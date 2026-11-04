#!/usr/bin/env python3
"""Download only public, hash-identical tokenizer assets; no Llama weights or account required."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import urllib.request

PUBLIC_REPO='mlx-community/Llama-3.2-3B-Instruct-bf16'
ORIGINAL_REPO='meta-llama/Llama-3.2-3B-Instruct'
FILES={
 'tokenizer.json':('5cc5f00a5b203e90a27a3bd60d1ec393b07971e8',9085657),
 'tokenizer_config.json':('4ff488a165e900e5129cda7c20ab32d568d2a475',54528),
 'special_tokens_map.json':('02ee80b6196926a5ad790a004d9efd6ab1ba6542',296),
}

def get(url):
    with urllib.request.urlopen(url,timeout=30) as response:return response.read()


def git_blob_sha(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def prepare(out,config_out):
    out=Path(out).resolve();out.mkdir(parents=True,exist_ok=True)
    meta=json.loads(get('https://huggingface.co/api/models/'+PUBLIC_REPO));revision=meta['sha']
    tree=json.loads(get('https://huggingface.co/api/models/'+ORIGINAL_REPO+'/tree/0cb88a4f764b7a12671c53f0838cd831a0843b95'))
    expected={x['path']:x for x in tree}
    checks=[]
    for name,(sha,size) in FILES.items():
        # Public metadata of the original model is readable even when downloads require approval.
        if expected[name]['oid']!=sha or expected[name]['size']!=size:
            raise RuntimeError('original revision metadata differs; refusing unverified substitution')
        dest=out/name
        data=dest.read_bytes() if dest.exists() else get(f'https://huggingface.co/{PUBLIC_REPO}/resolve/{revision}/{name}')
        if len(data)!=size or git_blob_sha(data)!=sha:
            raise RuntimeError(name+' differs from original bytes; no config written')
        dest.write_bytes(data)
        checks.append({'file':name,'size':size,'git_blob_sha1':sha,'sha256':hashlib.sha256(data).hexdigest(),'matches_original':True})
    # Download official MoshiRAG JSON only, not its multi-GB model weights.
    config_repo='kyutai/moshika-rag-pytorch-bf16';config_revision='7135a6e3c46abb66c2cd95cb04cbfcbe8376f83d'
    cfg=json.loads(get(f'https://huggingface.co/{config_repo}/resolve/{config_revision}/config.json'))
    conditioners=cfg.get('conditioners',{});changed=[]
    for name,c in conditioners.items():
        if c.get('type') in {'arc_encoder','multi_arc_encoder'}:
            sub=c[c['type']];sub['tokenizer_name']=str(out);changed.append(name)
    if not changed:raise RuntimeError('no ARC conditioner found; review source config')
    config_out=Path(config_out).resolve();config_out.parent.mkdir(parents=True,exist_ok=True)
    config_out.write_text(json.dumps(cfg,indent=2)+'\n')
    report={'original_repo':ORIGINAL_REPO,'original_revision':'0cb88a4f764b7a12671c53f0838cd831a0843b95',
            'public_repo':PUBLIC_REPO,'public_revision':revision,'files':checks,
            'conditioners_updated':changed,'config':str(config_out),'tokenizer_path':str(out),
            'scope':'Tokenizer asset identity only; not a reference-encoder/model inference test.'}
    (out/'identity_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='artifacts/arc_tokenizer');ap.add_argument('--config-out',default='artifacts/moshirag.local.json');a=ap.parse_args();prepare(a.out,a.config_out)
