import json,os

PATH=os.path.join(os.path.dirname(__file__),"data","weights.json")

def load_weights():
 with open(PATH) as f:
  return json.load(f)

def save_weights(w):
 with open(PATH,"w") as f:
  json.dump(w,f,indent=2)

def normalize(w):
 total=sum(w.values())
 for k in w:
  w[k]=round(w[k]/total,4)
 return w

def adjust_weights(trends,w):

 for t in trends:

  spread=len(t.get("sources",[]))
  freq=t.get("count",1)

  if spread>=3:
   w["spread"]+=0.01

  if freq>=4:
   w["frequency"]+=0.01

  if spread==1 and freq<=2:
   w["growth"]-=0.005

 for k in w:
  w[k]=max(w[k],0.05)

 return normalize(w)
