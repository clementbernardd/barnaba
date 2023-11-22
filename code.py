import barnaba as bb
from barnaba import escore

pred = "input/MODEL_1/3dRNA-1Z43-10.pdb"
native = "input/NATIVE/1Z43.pdb"

ermsd = bb.ermsd(native, pred)
native_escore = escore.Escore([native])
pred_escore = native_escore.score(pred)
rmsd_pred = bb.rmsd(native,pred)
print(ermsd)
print(pred_escore)
print(rmsd_pred)

