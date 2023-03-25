# Transforming-lambda-NFA-to-DFA
<h2>About</h2>
<p>This program implements the algorithm for transforming a lambda-NFA(NFA with NULL transition) into a DFA as well as a word parser for the automata.</p>
<p>All throughout the code the lambda symbol is reprezented by '$'.</p>
<h2>Input</h2>
<h3>The characteristics of the NFA/DFA have to be written in the <i>automata.in</i> file as such:</h3>
<p>Q - the set of states</p>
<p>Sigma - the alphabet</p>
<p>q0 - the intial state</p>
<p>F - the final states</p>
<p>delta - the transition function</p>
<p></p>
<p>Here is an example:</p>
<img src=https://user-images.githubusercontent.com/116015361/227747085-77213c0f-60b0-4393-ad33-ede2310c08d2.png>
<p></p>
<p></p>
<h3>The words which are to be parsed will be written in the <i>words.in</i> file.
<h2>Output</h2>
<p>The to_dfa_table function will return a dictionary reprezenting the delta function of the new dfa, the new initial state and the new final states of the dfa.</p> 


