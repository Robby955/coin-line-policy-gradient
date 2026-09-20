"""Two-exponential transition model; valid as a candidate local limit only.

A blow-up of this reduced flow is not proof of crossing in the full flow.
The approximation changes when b passes through zero.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from verify_zero_diversity_ray import parameters

ROOT=Path(__file__).resolve().parent


def main():
    zero=json.loads((ROOT/'results/zero-diversity-ray-20260919.json').read_text())
    full=[json.loads(s) for s in (ROOT/'results/correction-time-small-eps-20260919.jsonl').read_text().splitlines()]
    rows=[]
    x=np.array([1.,2.,1.])
    for L in [4,5,6]:
        u,C=parameters(L);C=float(C);M=u@u;D=u@x;X=x@x
        beta=D/M;alpha=1/(1-beta);B=1/(L*(L+1))
        offset=np.array(next(r for r in zero['trajectory_checks'] if r['L']==L and r['log1p_t']==600)['ray_offset'])
        tau0=1e-7
        y0=u/M*np.log(tau0)+offset
        def stop(t,y):return float(x@y+12)
        stop.direction=-1;stop.terminal=True
        sol=solve_ivp(lambda t,y:C*np.exp(-u@y)*u-B*np.exp(-x@y)*x,
                      (tau0,1000),y0,events=stop,method='DOP853',rtol=1e-10,atol=1e-12,max_step=.1)
        assert sol.success and len(sol.t_events[0])
        end=sol.y_events[0][0]
        rstar=(M-D)/(D-X)
        V=(u-rstar*x)/(M-D*rstar)
        W=alpha*u/M
        # Ray extrapolation only: compare b=0 and P=0 along W-s V.
        k=(L+1)//2
        b_switch=W[1]/V[1]
        probe_cross=(W[0]+k*W[1])/(V[0]+k*V[1])
        uminus=u[0]*np.array([1.,L-1.,L])
        Mm=uminus@uminus;Dm=uminus@x
        rm=(Mm-Dm)/(Dm-X)
        Vm=(uminus-rm*x)/(Mm-Dm*rm)
        W1=W-b_switch*V
        Wcross=W1-(W1[0]+k*W1[1])/(Vm[0]+k*Vm[1])*Vm
        rows.append({'second_phase_score':uminus.tolist(),
                     'second_phase_direction':Vm.tolist(),
                     'predicted_scaled_b_zero_state':W1.tolist(),
                     'predicted_scaled_crossing_state':Wcross.tolist(),
                     'observed_scaled_crossing_state':(np.array(next(z for z in full if z['L']==L and z['eps']==1e-96)['w_cross'])/(96*np.log(10))).tolist(),
                     'L':L,'beta':float(beta),'alpha':float(alpha),
                     'reduced_q_minus12_time':float(sol.t_events[0][0]),
                     'ratio_at_event':float(B/C*np.exp(u@end-x@end)),
                     'ratio_equilibrium':float(rstar),'blowup_direction':V.tolist(),
                     'extrapolated_b_zero_distance':float(b_switch),
                     'extrapolated_probe_zero_distance':float(probe_cross),
                     'full_rescaled_crossings':[{'eps':r['eps'],'eps_alpha_T':float(np.exp(r['log1p_t_cross']+alpha*np.log(r['eps'])))} for r in full if r['L']==L]})
    out=ROOT/'results/transition-model-two-phase-20260919.json'
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    out=args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps(rows,indent=2))

if __name__=='__main__':main()
