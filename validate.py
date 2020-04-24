PRED_FILE = 'predictions.txt'
RES_FILE = 'test_res.txt'

pred_file = open(PRED_FILE, 'r')
res_file = open(RES_FILE, 'r')

predictions = pred_file.readlines()
results = res_file.readlines()

correct = 0
total = len(predictions)
for i in range(total):
    p = int(predictions[i])
    r = [int(n) for n in results[i].split()]
    if p in r:
        correct += 1
    else:
        print(f'Incorrect prediction: {p} not in {r}')
print(f'Accuracy: {correct}/{total} = {1.0 * correct / total}')