# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Building a Simple Simulation in GNU Radio

# <markdowncell>

# Download the [Python script](./GNURadioforSimulation.py). or the [IPython](./GNURadioforSimulation.ipynb) notebook.

# <markdowncell>

# This document provides a walk-through for how to set up a GNU Radio flowgraph to run a simple simulation. While GNU Radio is designed for real-time, continuous use, there are many situations (testing, development, education, etc.) where we want to simulate signals and behavior of blocks. The difference is that we intend to run a flowgraph for a finite, and probably short, period of time. This tutorial will set up a simple top_block and generate, store, and then plot a noisy signal.
# 
# Before we begin any program, let's pull in the necessary Python modules. GNU Radio is composed of many modules with the main runtime and data type definitions found in <b>gnuradio.gr</b>. We pull in other GNU Radio modules that contain various signal processing blocks like <b>blocks</b>, which holds math, type conversions, and general utility blocks, and <b>analog</b>, which hold blocks related to analog signals and analog modulation.

# <codecell>

%matplotlib inline
from gnuradio import gr                # Pull in the GNU Radio runtime system
from gnuradio import blocks, analog    # Get some of the GNU Radio block modules
import scipy                           # Some useful tools for handling the data 
import matplotlib.pyplot as plt

# <headingcell level=2>

# Building the Top Block and Signal Processing Blocks

# <markdowncell>

# The following builds a default top_block and sets up some variables we will use later on.

# <codecell>

tb = gr.top_block()   # the top container class for a flowgraph

samp_rate = 32e3      # the sample rate of the system
freq = 1e3            # the frequency of the signal.
amp = 1               # the signal amplitude
namp = 0.1            # the amplitude of the noise source (variance of the Gaussian signal)
N = 10000             # number of samples to run in this simulation

# <markdowncell>

# We will construct a signal source block that generates a sine wave (<b>analog.GR_SIN_WAVE</b>) and pass it the above variables to set the properties.
# 
# In GNU Radio, the sample rate is almost a meaningless number. The GPP has no concept of sample timing, so there is no clock running at this rate. We use the concept of a sample rate as convenience to the user, which allows us to specify frequencies in terms of Hz instead of a normalized frequency. In reality, this signal generator uses the frequency of freq/samp_rate.

# <codecell>

signal = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, freq, amp)

# <markdowncell>

# Create a noise source that generates complex Gaussian random values with variance namp.

# <codecell>

noise = analog.noise_source_c(analog.GR_GAUSSIAN, namp)

# <markdowncell>

# Add the sine wave and the Gaussian values together.
# 
# Note that here we specify <b>_cc</b> as a suffix, which says that this block takes in and produces complex sample streams.

# <codecell>

add = blocks.add_cc()

# <markdowncell>

# Limit the number of samples produced to <i>N</i>. When this block counts <i>N</i> samples, it will stop the flowgraph. Since this is a simulation and we only want to generate so many samples, the head block is a convenient way of handling this. GNU Radio flowgraphs will run until stopped by an external event or when something explicitly tells it to. Otherwise, the signal and noise sources  will just keep producing new samples.

# <codecell>

head = blocks.head(gr.sizeof_gr_complex, N)

# <markdowncell>

# Now we want to store the data so we can use Matplotlib tools to plot it. We use a vector_sink block which stores the data internally as a vector. This block can be dangerous because it simply keeps growing the vector. If there are no limits placed on it (like the head block above), it can quickly eat up your system's memory. It is only advisable to use this block when running a simulation and for post-analysis of data collections, but not for live streaming apps.

# <codecell>

sink = blocks.vector_sink_c()

# <headingcell level=2>

# Connecting and Running the Flowgraph

# <markdowncell>

# We now have a set of blocks that will form a flowgraph:
# 
# <pre>
# signal ->
#           add -> head -> sink
# noise  ->
# </pre>
# 
# We now need to connect these blocks together into an actual flowgraph that's held by the  top_block above. We just need to use the connect function of the top_block for this. The connect function takes the form <b>connect((source, port), (destination, port))</b> where the ports define which output or input port to use in the connection. If no port is specified, Python interprets it as port 0. In our flowgraph here, only the add block has multiple input ports. We'll connect <b>signal</b> to port 0 of <b>add</b> and connect <b>noise</b>' to port 1 of <b>add</b>.

# <codecell>

tb.connect(signal, (add,0))       # signal:0 to add:0
tb.connect((noise,0), (add,1))    # more explicit --> noise:0 to add:1
tb.connect(add, head, sink)       # convenience function to string together multiple blocks  

# <markdowncell>

# We now want to run our flowgraph. When we start it, it will start generating samples in the  signal and noise sources and run the samples down stream in the flowgraph. We can start the flowgraph in one of two ways:
# 
# * <b>tb.start()</b>:
# This is a non-blocking call that launches the top_block as a thread to run the scheduler. It returns immediately and allows us to continue our program while the flowgraph is running.
# 
# * <b>tb.run()</b>:
# This is a blocking call. It starts the top_block thread and waits until it finishes before returning. This is useful for us in a simulation like this where we want it to complete processing all N samples.
# 
# The top_block also has a <b>tb.wait()</b> function. This is used to block on the <b>top_block</b>'s thread. If we've started using <b>tb.start()</b> and are finished with "our" program and need to wait for the flowgraph to finish, we can call the wait function to do this. In reality, <b>tb.run()</b> is just an alias for <b>tb.start(); tb.wait()</b>.

# <codecell>

tb.run()

# <headingcell level=2>

# Extracting and Plotting the Data

# <markdowncell>

# It's now time to get the data out of the flowgraph. The vector_sink block has stored all of the samples into an internal vector. We retrieve it by calling the <b>data()</b> function on the object. This returns the vector to us as a Python list. We'll wrap the data into a Scipy array to make later manipulations easier and then print out just the first 10 samples.

# <codecell>

data = scipy.array(sink.data())
print data[0:10]

# <markdowncell>

# Now we want to plot the data. Let's plot a few hundred samples of the real and imaginary parts of the noisy sine wave as well as a histogram of signal over 100 bins.

# <codecell>

fig = plt.figure(1, figsize=(10,10))
sp1 = fig.add_subplot(2,1,1)
sp2 = fig.add_subplot(2,1,2)

sp1.plot(data.real[100:300], 'b')
sp1.plot(data.imag[100:300], 'r')
h = sp2.hist(data, 100)

# <codecell>


