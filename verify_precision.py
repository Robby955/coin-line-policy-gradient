"""Reproduce high-precision gradient checks at the smallest-diversity crossings."""
import argparse
import json
from pathlib import Path
import mpmath as mp
import numpy as np
from model import objective
from validate_saturation import reference


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    mp.mp.dps=180
    root=Path(__file__).resolve().parent
    rows=[]
    for row in map(json.loads,(root/'results/correction-time-small-eps-20260919.jsonl').read_text().splitlines()):
        if row['eps']!=1e-96:continue
        L=row['L'];w=row['w_cross']
        ref=reference(w,L,'1e-96');got=objective(w,L,1e-96)[1]
        error=float(np.max(np.abs(got-ref)/np.abs(ref)))
        np.testing.assert_allclose(got,ref,rtol=1e-10,atol=0)
        rows.append({'L':L,'eps':1e-96,'digits':180,'max_relative_gradient_error':error})
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps(rows,indent=2))

if __name__=='__main__':main()
