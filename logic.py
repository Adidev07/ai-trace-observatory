import math
def run(payload, records):
    threshold=float(payload.get('latency_threshold_ms',1500))
    if not math.isfinite(threshold) or threshold<=0: raise ValueError('Threshold must be positive and finite')
    model=str(payload.get('model','all')).strip()
    rows=[r for r in records if model=='all' or r['model']==model]
    latencies=sorted(r['latency_ms'] for r in rows)
    p95=latencies[max(0,math.ceil(.95*len(latencies))-1)] if rows else None
    errors=sum(r['status']!='ok' for r in rows)
    alerts=[dict(trace_id=r['trace_id'],reason='request error' if r['status']!='ok' else 'slow request') for r in rows if r['status']!='ok' or r['latency_ms']>threshold]
    return dict(count=len(rows),error_rate=round(errors/len(rows),3) if rows else 0,p95_latency_ms=p95,total_tokens=sum(r['input_tokens']+r['output_tokens'] for r in rows),estimated_cost_usd=round(sum((r['input_tokens']*r['input_usd_per_million']+r['output_tokens']*r['output_usd_per_million'])/1_000_000 for r in rows),6),alerts=alerts,traces=rows,note='Synthetic traces and illustrative rates, not current provider pricing. No prompts or secrets are logged.')
