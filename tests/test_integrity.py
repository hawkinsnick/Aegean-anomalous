import json,pathlib
R=pathlib.Path(__file__).parents[1]
def L(p): return json.loads((R/p).read_text())
def test_neutrality():
 p=L('project.json'); a=L('research/admission-policy.json'); x=L('research/pre-expert-maximum.json')
 assert p['canonical_script_claims']==0 and len(a['initial_candidates'])>=2 and x['target']=='PRE_EXPERT_MAXIMUM'
 assert any('single script' in s for s in a['admission_does_not_mean'])
def test_release_assurance():
 for p in ['research/evidence-matrix.json','research/rights-register.json','research/source-dependence.json','research/expert-review-packet.json','research/candidate-register.json']: L(p)
 c=L('research/candidate-register.json')['candidates']; assert {x['id'] for x in c}>={'ARKALOCHORI-AXE','MALIA-ALTAR-STONE'}
 assert next(x for x in c if x['id']=='ARKALOCHORI-AXE')['official_museum_evidence']['evidence_class']=='OFFICIAL_MUSEUM_METADATA'
