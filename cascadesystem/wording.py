"""Conservative sentence wording without new facts or additional model calls."""
import re

from .presentation import finish_sentence


def clean_description(description):
    text = description.strip()
    text = re.sub(r'^(?:(?:identify|find|determine|check|confirm)\s+(?:out\s+)?)', '', text, flags=re.I)
    text = re.sub(r'^(?:请)?(?:确定|确认|查找|找出|查询|识别)\s*', '', text)
    return text.rstrip('。！？.!? ').strip()


def boolean_sentence(topic, value):
    """Express a few grammatical proposition forms, preserving literal Yes/No.

    Negating 'both' must negate the whole proposition, not assert that neither
    person has the property. Unknown forms retain the conservative fact frame.
    """
    if value.casefold() not in {'yes', 'no'}:
        return None
    positive = value.casefold() == 'yes'
    proposition = re.sub(r'^(?:whether|if)\s+', '', topic, flags=re.I)
    occupation = re.fullmatch(r"(.+?)'s occupation (?:as|includes)\s+(.+)", proposition, re.I)
    if occupation:
        person, role = occupation.groups()
        role = role if re.match(r'^(?:a|an|the)\b', role, re.I) else 'a ' + role
        return f"{value}, {person} is {'' if positive else 'not '}{role}"
    be = re.fullmatch(r'(.+?)\s+(is|are|was|were)\s+(.+)', proposition, re.I)
    belongs = re.fullmatch(r'(.+?)\s+(belong|belongs)\s+(.+)', proposition, re.I)
    if not (be or belongs):
        return None
    if positive:
        return f'{value}, {proposition}'
    if re.search(r'\b(?:both|all)\b', proposition, re.I):
        return f'{value}, it is not the case that {proposition}'
    subject, verb, rest = (be or belongs).groups()
    if be:
        return f'{value}, {subject} {verb} not {rest}'
    auxiliary = 'does' if verb.casefold() == 'belongs' else 'do'
    return f'{value}, {subject} {auxiliary} not belong {rest}'


def fact_sentences(facts, language, *, natural=True):
    sentences = []
    for fact in facts:
        description, value = fact['description'], fact['value']
        if not natural:
            sentences.append(f'{description}：{value}。' if language == 'zh' else f'{description}: {value}.')
            continue
        topic = clean_description(description) or ('这项信息' if language == 'zh' else 'The requested value')
        boolean = boolean_sentence(topic, value) if language != 'zh' else None
        if boolean:
            sentences.append(finish_sentence(boolean, language))
            continue
        if language == 'zh':
            if re.match(r'^(?:是否|谁|哪个|哪里|何时|什么时候)', topic):
                text = f'关于“{topic}”，目前能确认的答案是{value}'
            else:
                text = f'{topic}是{value}'
        elif re.match(r'^(?:whether|if|who|what|which|where|when|how)\b', topic, re.I):
            text = f'For the question "{topic}", the confirmed answer is {value}'
        else:
            if re.match(r'^(?:father|mother|parent|grandfather|grandmother|birthplace|nationality|country|name|date|year|job|occupation|family) of\b', topic, re.I):
                topic = 'The ' + topic[0].lower() + topic[1:]
            text = f'{topic[:1].upper() + topic[1:]} is {value}'
        sentences.append(finish_sentence(text, language))
    return ' '.join(sentences)


def label_style(text, facts):
    """Recognize copied unit-label/value pairs, without banning colons in titles or times."""
    for fact in facts:
        for description in [fact['description'], clean_description(fact['description'])]:
            pattern = re.escape(description) + r'\s*[:：]\s*' + re.escape(fact['value'])
            if re.search(pattern, text, re.I):
                return True
    return False


def missing_sentence(descriptions, language, *, natural=True):
    if not descriptions:
        return ''
    if not natural:
        names = '、'.join(description.rstrip('。！？.!? ') for description in descriptions)
        return f'目前无法确认：{names}。' if language == 'zh' else f'I could not confirm: {names}.'
    names = [clean_description(description) for description in descriptions]
    if language == 'zh':
        return finish_sentence('我目前还无法确认' + '、'.join(names), language)
    subject = names[0] if len(names) == 1 else ', '.join(names[:-1]) + ' and ' + names[-1]
    return finish_sentence('I could not confirm ' + subject, language)
