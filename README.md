# Barcode decoding with a neural network?


## Experiment 1: Decoding a single digit.

### Experiment 1a:

We are either performing *regression* on the input data or *classification*.
Here I run both methods, and see that *regression* isn't appropriate for this problem.
In retrospect this is obvious the outputs have no linear relationship to the outputs.

### Experiment 1b:

SKLearn usecases *one-hot* encoding for these multi-output classification problems. Which seems like it a good choice, but I would like to try other encodings, such as a binary encoding, i.e. encoding the output digit as a 4-bit number

**To-do: Finish off this experiment**
### Experiment 1c:

There is the concept of *batch-size* which (I think) is how many inputs we show to network before updating the weights.
Here I experiment with the size of the batches, finding that a batch size of 1 converges the fastest.

**To-do:  Better understanding of how and why the network converges fastest with a batchsize of 1**

I think this makes sense

### Experiment 1d:

What do the weights look like?
They have a clear relation to encoding.

**Write a good explanation of how this works**

### Experiment 1e:

What happens when we train with noisy data? What do the weights look like? How noisy before we get wrong answers.
This is related to where the decision boundaries are drawn?

### Coming experiments:


- Play around with *normalising* the data first.
- What happens when we include noise in the data?
- What happens when we include two different encodings?