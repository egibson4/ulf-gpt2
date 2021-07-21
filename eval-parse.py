import random

from transformers import GPT2DoubleHeadsModel, GPT2Tokenizer

model = GPT2DoubleHeadsModel.from_pretrained('./parse-output-large').to('cuda:0')
tok = GPT2Tokenizer.from_pretrained('gpt2-large')

evals = []
with open('input/parse_testing.txt', 'r') as f:
	evals = [x.strip() for x in f.readlines()]

random.shuffle(evals)

def ulf_to_eng(ulf):
	inp = tok(ulf + ' <SEP>', return_tensors='pt').input_ids.to('cuda:0')
	outp = tok.batch_decode(model.generate(inp, max_length=128, pad_token_id=50256))[0]
	outp = outp.split('<END>')[0]
	outp = outp.split('<SEP>')[1]
	outp = outp.strip()

	return outp

if __name__ == '__main__':
	for sent in evals:
		spl = sent.split(' <SEP> ')
		ulf = spl[0].strip()
		eng = spl[1].strip()

		print('sent: %s' % (ulf))
		print('want: %s' % (eng))
		print('got:  %s' % ulf_to_eng(ulf))
		print('', flush=True)
