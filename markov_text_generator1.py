import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

with open("trump_tweets.txt") as f:
    text = f.read()
model_a = markovify.Text(text, state_size=2)

with open("lovecraft.txt") as f:
    text = f.read()
model_b = markovify.Text(text, state_size=2)

model_combo = markovify.combine([model_a, model_b], [1.0, 20.0])







# Print randomly-generated sentences five
for i in range(100):
    print(model_combo.make_sentence())
    print ''