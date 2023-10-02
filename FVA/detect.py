import numpy as np

def formant_detect(input0, df0, f_min = 0):

  f_result = []
  i_result = []

  for i in range (1,len(input0)-1):
    if f_min is not None and df0 * i <= f_min: continue
    if input0[i] > input0[i-1] and input0[i] > input0[i+1]:
      f_result.append(df0 * i)
      i_result.append(i)
  
  return f_result, i_result

def pitch_detect(input0, dt0, ratio0 = 0.2, f_min = 100, f_max = 500):
  
  is_find_first = False
  f_result = []
  i_result = []
  v_result = []

  for i in range (1,len(input0)-1):
    if np.abs(input0[i]) < np.abs(input0[0] * ratio0): continue
    fp = 1.0 / (dt0 * i)
    if f_max is not None  and fp >= f_max: continue
    if f_min is not None and  fp <= f_min: continue
    if input0[i] > input0[i-1] and input0[i] > input0[i+1]:
      if not is_find_first:
        f_result.append(fp)
        i_result.append(i)
        v_result.append(input0[i])
        is_find_first = True
      else:
        f_result.append(fp)
        i_result.append(i)
        v_result.append(input0[i])
    elif input0[i] < input0[i-1] and input0[i] < input0[i+1]:
      if not is_find_first:
        f_result.append(fp)
        i_result.append(i)
        v_result.append(input0[i])
        is_find_first = True
      else:
        f_result.append(fp)
        i_result.append(i)
        v_result.append(input0[i])

  if is_find_first:
    a = np.argmax(np.array(v_result))
    f_result2 = [f_result[np.argmax( np.array(v_result))]]
    i_result2 = [i_result[np.argmax( np.array(v_result))]]
  else:
    f_result2 = []
    i_result2 = []
  return f_result2, i_result2