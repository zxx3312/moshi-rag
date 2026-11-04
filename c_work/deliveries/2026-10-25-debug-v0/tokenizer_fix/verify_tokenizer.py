#!/usr/bin/env python3
"""CPU-only tokenization test using the selected fork's real ArcEncoderTokenizer class body."""
import argparse
import ast
import json
import logging
from pathlib import Path
import typing as tp
from transformers import AutoTokenizer


def verify(repo,assets):
    source=Path(repo)/'moshi/moshi/conditioners/arc_encoder.py'
    tree=ast.parse(source.read_text());cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='ArcEncoderTokenizer')
    module=ast.Module(body=[cls],type_ignores=[]);ns={'AutoTokenizer':AutoTokenizer,'logger':logging.getLogger(__name__),'tp':tp}
    exec(compile(module,str(source),'exec'),ns)
    tokenizer=ns['ArcEncoderTokenizer'](str(Path(assets).resolve()))
    assert tokenizer.bos_token==128000 and tokenizer.eos_token==128009
    examples=['James Buchanan was the last U.S. president born in the 18th century.',
              'The museum closes at 5 PM. Adult admission costs $12.',
              '检索资料尚未全部到达。','Café résumé — déjà vu.','']
    result=[]
    for text in examples:
        ids=tokenizer.encode(text);decoded=tokenizer.decode(ids)
        if decoded!=text:raise RuntimeError('round trip failed: '+repr(text))
        if any(i<0 or i>=128256 for i in ids):raise RuntimeError('ID exceeds ARC embedding rows')
        result.append({'text':text,'ids':ids,'round_trip':True})
    assert tokenizer.encode('hello',bos=True,eos=True)[0]==128000
    assert tokenizer.encode('hello',bos=True,eos=True)[-1]==128009
    report={'status':'PASS','loaded_class':'real ArcEncoderTokenizer extracted from audited source',
            'torch_or_model_loaded':False,'bos':tokenizer.bos_token,'eos':tokenizer.eos_token,
            'base_vocab_size':tokenizer.vocab_size,'examples':result,
            'scope':'Tokenizer identity and runtime only, not ARC tensor or Moshi generation verification.'}
    print(json.dumps(report,ensure_ascii=False,indent=2));return report

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--assets',required=True);a=ap.parse_args();verify(a.repo,a.assets)
