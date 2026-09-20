"""Reproduce the rate table and plot from the retained experiment receipts."""
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent

def read(name):
    return [json.loads(s) for s in (ROOT/'results'/name).read_text().splitlines()]

def predicted(L):
    n=(L+2)//2
    r=n-int(L%2==0)
    norm=n*n*(1+L*L)+r*r
    dot=n*(L+1)+2*r
    return Fraction(norm,norm-dot)

def main():
    rows=read('correction-time-pilot-20260919.jsonl')+read('correction-time-small-eps-20260919.jsonl')
    validation=read('correction-time-validation-20260919.jsonl')
    comparisons=[]
    for check in validation:
        original=next(r for r in rows if r['L']==check['L'] and r['eps']==check['eps'])
        comparisons.append({'L':check['L'],'eps':check['eps'],
                            'relative_time_change':abs(check['t_cross']/original['t_cross']-1)})
    fig,axes=plt.subplots(1,2,figsize=(10,4),layout='constrained')
    summary=[]
    for L in [4,5,6]:
        part=sorted([r for r in rows if r['L']==L],key=lambda r:-r['eps'])
        x=np.log([1/r['eps'] for r in part])
        y=np.log([r['t_cross'] for r in part])
        slope=np.diff(y)/np.diff(x)
        alpha=predicted(L)
        line,=axes[0].plot(x/np.log(10),y/np.log(10),'o-',label=f'L={L}')
        axes[1].plot((x[1:]+x[:-1])/(2*np.log(10)),slope,'o-',color=line.get_color(),label=f'L={L}')
        axes[1].axhline(float(alpha),ls='--',color=line.get_color(),alpha=.7)
        summary.append({'L':L,'conjectured_exponent_exact':str(alpha),'conjectured_exponent':float(alpha),
                        'last_secant_exponent':float(slope[-1]),'eps_interval':[part[-2]['eps'],part[-1]['eps']]})
    axes[0].set(xlabel='log10(1 / diversity)',ylabel='log10(first correction time)')
    axes[1].set(xlabel='Midpoint log10(1 / diversity)',ylabel='Local log-log slope',title='Dashed: predicted exponents')
    for ax in axes:ax.legend();ax.grid(alpha=.2)
    (ROOT/'output/figures').mkdir(parents=True,exist_ok=True)
    fig.savefig(ROOT/'output/figures/correction-time-scaling.png',dpi=170)
    fig.savefig(ROOT/'output/figures/correction-time-scaling.pdf')
    result={'exponents':summary,'solver_comparison':comparisons}
    (ROOT/'results/correction-time-summary-20260919.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
