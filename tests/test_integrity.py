import json,pathlib
R=pathlib.Path(__file__).parents[1]
def L(p): return json.loads((R/p).read_text())
def test_neutrality():
 p=L('project.json'); a=L('research/admission-policy.json'); x=L('research/pre-expert-maximum.json')
 assert p['canonical_script_claims']==0
 assert len(a['initial_candidates'])>=2
 assert x['target']=='PRE_EXPERT_MAXIMUM'
 assert any('single script' in s for s in a['admission_does_not_mean'])
