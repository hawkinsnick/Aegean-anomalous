#!/usr/bin/env python3
import json,pathlib,sys
R=pathlib.Path(__file__).resolve().parents[1];out=pathlib.Path(sys.argv[1]);v=json.loads((R/"research/candidate-register.json").read_text());out.write_text(json.dumps(v["candidates"],ensure_ascii=False,indent=2)+"\n");out.with_suffix(out.suffix+".manifest.json").write_text(json.dumps({"candidates":len(v["candidates"]),"canonical_script_claims":0,"boundary":"Quarantine export; third-party images/models excluded."},indent=2)+"\n")
