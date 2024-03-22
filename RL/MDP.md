 # Markov Decision Processes
Requirements: None
## Resources
- [Sutton & Barto 3.1 - 3.4](http://incompleteideas.net/book/RLbook2020.pdf)
- [ML@B Blog](https://ml.berkeley.edu/blog/posts/mdps/)
- [Towards Data Science](https://towardsdatascience.com/introduction-to-reinforcement-learning-markov-decision-process-44c533ebf8da)

## Introduction
One goal of the field of Artificial Intelligence is to automate certain tasks which are currently completed by humans. To approach this problem, it is helpful to be able to generalize these distinct tasks into a single framework. 

To understand how to choose the proper framework, let's think about the limitations of the machines we will attempt to use to solve tasks in this framework. 

First of all, unlike humans, whose internal neural dynamics respond continuously to the environment, computers can only respond at discrete time steps (clock cycles). 

Secondly, it is unclear how to communicate the intended task to our computers; they don't understand natural language by default. Even if we try to teach them how to speak our language (e.g. LLMs), natural language is complex and misinterpretable, and we don't want our computers to act like the Genie from Aladdin when a user isn't specific enough. We will thus need a simpler signal to tell the computer when it is succeeding and failing at the task.

With these drawbacks in mind, we propose the **Markov Decision Process** (MDP). In this model, we have an **agent** interacting with an **environment** over discrete time steps, attempting to maximize its expected **reward**. At any discrete time step, three things happen in immediate succession:
1. The agent is in a **state**
2. The agent takes an **action**, moving it to a new state
3. The agent receives a numerical **reward** corresponding to the state and action in parts (1) and (2)

As this cycle repeats, the agent traces out a **trajectory** $\tau = ((s_0, a_0), \dots, (s_t, a_t))$, or list of states and actions, in the MDP. We use discrete time steps since our computers respond discretely to their surroundings, and we use a simple numerical reward as the representation of the task in order to give the computer a simple signal that both the computer and onlooking humans can understand.

## Definition
More concretely, An MDP is a tuple $(\mathcal S, \mathcal A, \mathcal{T}, r, \mu_0)$, meaning it consists of 
1. A **State Space** $\mathcal S$, the set of all of the states in which the agent could possibly be
2. An **Action Space** $\mathcal A$, the set of all the actions the agent could possibly take in each state
3. A **Transition Operator** $\mathcal{T} : \mathcal S\times \mathcal A \to \mathcal{D}(\mathcal S)$, which defines the distribution $\mathcal{T}(s' \mid s, a)$ over possible next states $s'$ given the current state $s$ and the action $a$ just taken
4. A **Reward Function** $r: \mathcal S\times \mathcal A\to \mathbb{R}$, which determines the reward $r(s, a)$ received by the agent when it takes action $a$ in state $s$
5. An **Initial State Distribution** $\mu_0$ over $\mathcal S$, from which the starting state is sampled: $s_0\sim\mu_0$.
Note that the reward function only depends on the current state-action pair $(s_t, a_t)$, and not the previous states or actions in our current trajectory. This is known as the **Markov Property** and is what distinguishes a regular old Decision Process from an MDP.

### Describing Solutions
To *solve* an MDP, we would like to know which actions to take in order to maximize expected total reward over many timesteps. Formally, a possible solution to an MDP is represented by a **policy** $\pi: \mathcal S\to \mathcal{D}(\mathcal A)$. The policy tells us the distribution over actions taken by the agent: at each time step, when the agent with policy $\pi$ begins in a state $s$, it will sample an action $a\sim\pi(s)$ from the policy and take this action. 

A path taken across an MDP is formalized as a **trajectory**, or a sequence of state-action pairs
$$\tau = ((s_0, a_0), (s_1, a_1), \dots (s_T, a_T))$$
The trajectory shown has finite **horizon** $T$, meaning the number of steps we take in the environment. A policy $\pi$ induces a distribution $\mathcal{T}^{\pi}$ over trajectories:
$$\mathcal{T}^{\pi}(\tau \mid s_0) = \prod_{k=0}^{T}\pi(a_k\mid s_k) \mathcal{T}(s_{k+1}\mid s_k, a_k)$$
$$\mathcal{T}^{\pi}(\tau \mid s_0, a_0) = \prod_{k=0}^{T} \mathcal{T}(s_{k+1}\mid s_k, a_k)\pi(a_{k+1}\mid s_{k+1})$$
These equations effectively define sampling processes: the first says, starting with $s_0$, first sample $a_0\sim \pi(a_0\mid s_0)$, then sample $s_1 \sim \mathcal{T}(s_1\mid s_0, a_0)$, then sample $a_1 \sim \pi(a_1\mid s_1)$, and so on. This sampling process gives rise to the distribution $\mathcal{T}^{\pi}(\tau\mid s_0)$. Similarly, the sampling process beginning with $s_1\sim\mathcal{T}(s_1\mid s_0, a_0)$ gives rise to the distribution $\mathcal{T}^{\pi}(\tau\mid s_0, a_0)$.

Using these distributions, we can write the maximization objective corresponding to this MDP with horizon $T$ as
$$\max_{\pi}\mathop{\mathbb E}_{\tau\sim \mathcal{T}^{\pi}(\tau\mid s)}\sum_{t=0}^T r(s_t, a_t)$$

Note there is some optimal policy $\pi^*$ which maximizes this objective. We let $\mathcal{T}^*$ refer to the distribution over trajectories under the optimal policy, so $\mathcal{T}^* = \mathcal{T}^{\pi^*}$. Then we have
$$\mathcal{T}^*(\tau \mid s_0) = \prod_{k=0}^{\infty}\pi^*(a_k\mid s_k) \mathcal{T}(s_{k+1}\mid s_k, a_k)$$
$$\mathcal{T}^*(\tau \mid s_0, a_0) = \prod_{k=0}^{\infty} \mathcal{T}(s_{k+1}\mid s_k, a_k)\pi^*(a_{k+1}\mid s_{k+1})$$

### Decomposing Expectations
Notice that our maximization objective involves an expectation over the distribution of trajectories $\mathcal{T}^{\pi}(\tau\mid s)$. Recall a trajectory $\tau$ is a list of states and actions:
$$\tau = ((s, a_0), (s_1, a_1), \dots (s_T, a_T))$$
where $s$ is given. Hence, taking an expectation over a distribution over $\tau$ is identical to taking an expectation over $a_0, s_1, a_1, \dots$ and so on:
$$\mathop{\mathbb E}_{\tau\sim\mathcal{T}(\tau\mid s)} =\underset{\substack{a_0 \sim \pi(a_0\mid s)\\s_1\sim \mathcal{T}(s_1\mid s, a_0)\\a_1 \sim \pi(a_1\mid s_1)\\\vdots}}{\mathbb{E}} = \mathop{\mathbb E}_{a_0 \sim \pi(a_0\mid s)}\;\mathop{\mathbb E}_{s_1\sim \mathcal{T}(s_1\mid s, a_0)}\;\mathop{\mathbb E}_{a_1\sim \pi(a_1\mid s_1)}\dots$$
We are able to decompose the expectation over trajectories into this series of expectations over states and actions because 
- the distribution of $a_0$ only depends on the value of $s$,
- the distribution of $s_1$ depends only on $s$ and $a_0$, 
- the distribution of $a_1$ depends only on $s_1$, and so on.

More generally, we can decompose an expectation over $\mathcal{T}^{\pi}$ into **alternating** expectations over $\pi$ and $\mathcal{T}$:
$$\begin{align*}\mathop{\mathbb E}_{\tau \sim \mathcal{T}^{\pi}(\tau \mid s)} &= \mathop{\mathbb E}_{a_0\sim \pi(s)}\;\mathop{\mathbb E}_{s_1\sim \mathcal{T}(s_1\mid s, a_0)}\;\mathop{\mathbb E}_{a_1\sim \pi(s_1)}\;\mathop{\mathbb E}_{s_2\sim \mathcal{T}(s_2\mid s_1, a_1)} \dots\\
\mathop{\mathbb E}_{\tau \sim \mathcal{T}^{\pi}(\tau \mid s, a)} &= \mathop{\mathbb E}_{s_1\sim \mathcal{T}(s_1\mid s, a)}\;\mathop{\mathbb E}_{a_1\sim \pi(s_1)}\;\mathop{\mathbb E}_{s_2\sim \mathcal{T}(s_2\mid s_1, a_1)}\;\mathop{\mathbb E}_{a_2\sim \pi(s_2)} \dots\end{align*}$$
Similarly, we can break an expectation over $\mathcal{T}^*$ into **alternating** expectations over $\pi^*$ and $\mathcal{T}$:
$$\begin{align*}\mathop{\mathbb E}_{\tau \sim \mathcal{T}^*(\tau \mid s)} &= \mathop{\mathbb E}_{a_0\sim \pi^*(s)}\;\mathop{\mathbb E}_{s_1\sim \mathcal{T}(s_1\mid s, a_0)}\;\mathop{\mathbb E}_{a_1\sim \pi^*(s_1)}\;\mathop{\mathbb E}_{s_2\sim \mathcal{T}(s_2\mid s_1, a_1)} \dots\\
\mathop{\mathbb E}_{\tau \sim \mathcal{T}^*(\tau \mid s, a)} &= \mathop{\mathbb E}_{s_1\sim \mathcal{T}(s_1\mid s, a)}\;\mathop{\mathbb E}_{a_1\sim \pi^*(s_1)}\;\mathop{\mathbb E}_{s_2\sim \mathcal{T}(s_2\mid s_1, a_1)}\;\mathop{\mathbb E}_{a_2\sim \pi^*(s_2)} \dots\end{align*}$$
In most situations we don't know $\pi^*$, so this decomposition is useless. However, in the original maximization objective, we are taking the expectation of the total reward, and $\pi^*$ is the policy which maximizes the total reward. Therefore we can write
$$\begin{align*}\mathop{\mathbb E}_{\tau \sim \mathcal{T}^*(\tau \mid s)}\Bigg[\sum_{t=0}^Tr(s_t, a_t)\Bigg] &= \max_{a_0\in \mathcal A}\;\mathop{\mathbb E}_{s_1\sim \mathcal{T}(s_1\mid s, a_0)}\;\max_{a_1\in \mathcal A}\;\mathop{\mathbb E}_{s_2\sim \mathcal{T}(s_2\mid s_1, a_1)} \dots\Bigg[\sum_{t=0}^Tr(s_t, a_t)\Bigg]\\
\mathop{\mathbb E}_{\tau \sim \mathcal{T}^*(\tau \mid s, a)}\Bigg[\sum_{t=0}^Tr(s_t, a_t)\Bigg] &= \mathop{\mathbb E}_{s_1\sim \mathcal{T}(s_1\mid s, a)}\;\max_{a_1\in \mathcal A}\;\mathop{\mathbb E}_{s_2\sim \mathcal{T}(s_2\mid s_1, a_1)}\;\max_{a_2\in \mathcal A} \dots\Bigg[\sum_{t=0}^Tr(s_t, a_t)\Bigg]\end{align*}$$
### Sampling from Trajectories
Suppose we wanted to sample individual states from our trajectories. When we build learning algorithms to solve MDPs, this is necessary since our learning algorithms will train on previously seen states. Given that our trajectories start at a state $s_0$, what di
# finish section on state visitation distributions!!

### Infinite Horizon MDPs

Sometimes, we would like find a policy which maximizes reward-to-go infinitely far in the future: we would like to set the horizon $T = \infty$. Note that then the expected total rewards over our infinitely long trajectories can grow unboundedly, so there may be no policy $\pi$ which maximizes expected total reward. How can we get around this?

This problem did not arise  for finite horizon $T$, because if rewards have value at most $R$, then our total reward over any trajectory is bounded by $RT$. We can induce a similar bound for the infinite-horizon case by introducing a **discount factor** $\gamma$. This means we multiply the reward term from taking action $a_t$ in state $s_t$ by $\gamma^t$, yielding the objective$$\max_{\pi}\mathop{\mathbb E}_{\tau\sim \mathcal{T}^{\pi}(\tau\mid s)}\Bigg[\sum_{t=0}^\infty \gamma^tr(s_t, a_t)\Bigg]$$Intuitively, this means we value rewards obtained soon over rewards obtained far into the future. Now, when rewards have value at most $R$, our total reward over any trajectory is bounded by $\frac{R}{1-\gamma}$. Notice that $\frac{1}{1-\gamma}$ takes the place of $T$: it is the **effective horizon** of the infinite MDP, and in RL Theory, we'll often see that the same theorems that hold for infinite MDPs with discount factor $\gamma$ also hold for finite MDPs with horizon $T = \frac{1}{1-\gamma}$.

***Note: This changes the optimal policy.*** Specifically, the optimal policy now takes actions which maximize expected *discounted* total reward. This means we can still replace expectations over the optimal policy with maximums over the action space, as done above: ^0c1458
$$\begin{align*}\mathop{\mathbb E}_{\tau \sim \mathcal{T}^*(\tau \mid s)}\Bigg[\sum_{t=0}^\infty \gamma^tr(s_t, a_t)\Bigg] &= \max_{a_0\in \mathcal A}\;\mathop{\mathbb E}_{s_1\sim \mathcal{T}(s_1\mid s, a_0)}\;\max_{a_1\in \mathcal A}\;\mathop{\mathbb E}_{s_2\sim \mathcal{T}(s_2\mid s_1, a_1)} \dots\Bigg[\sum_{t=0}^\infty \gamma^tr(s_t, a_t)\Bigg]\\
\mathop{\mathbb E}_{\tau \sim \mathcal{T}^*(\tau \mid s, a)}\Bigg[\sum_{t=0}^\infty \gamma^tr(s_t, a_t)\Bigg] &= \mathop{\mathbb E}_{s_1\sim \mathcal{T}(s_1\mid s, a)}\;\max_{a_1\in \mathcal A}\;\mathop{\mathbb E}_{s_2\sim \mathcal{T}(s_2\mid s_1, a_1)}\;\max_{a_2\in \mathcal A} \dots\Bigg[\sum_{t=0}^\infty \gamma^tr(s_t, a_t)\Bigg]\end{align*}$$
#### Infinite-Horizon MDPs: An Alternative Formulation
The discount factor introduced above seems poorly motivated: we introduced it to preserve bounded rewards in infinite-horizon MDPs, but there are many reweightings of reward that could accomplish this (e.g. $t \gamma^{t}$ rather than $\gamma^{t}$).

Here we introduce another way to view the discount factor. Suppose we modify our MDP by introducing a state $d$ known as the death state. We will modify the transition function as follows:
$$\mathcal{T}'(s'\mid s, a) = \gamma \mathcal{T}(s'\mid s, a) + (1 - \gamma) \mathbb{1}(s' = d)$$
That is, every timestep, our new transition function $\mathcal{T}'$ sends us to the same state as $\mathcal{T}$ with probability $\gamma$, but sends us to the death state and ends our rollout with probability $1 - \gamma$. Now note that the MDP is the same as before, but the probability we make it to timestep $t$ is scaled by $\gamma^t$. Thus timestep $t$'s expected contribution to total reward is also scaled by $\gamma^t$, and so

$$\mathop{\mathbb E}_{\tau\sim \mathcal{T}'(\tau\mid s)}\Bigg[\sum_{t=0}^\infty r(s_t, a_t)\Bigg] = \mathop{\mathbb E}_{\tau\sim \mathcal{T}(\tau\mid s)}\Bigg[\sum_{t=0}^\infty \gamma^tr(s_t, a_t)\Bigg]$$

Thus, introducing a discount factor is equivalent to solving for maximum expected total reward in the modified MDP with the death state. In essence, $\gamma$ sets the probability that something goes wrong unexpectedly, ending the trajectory prematurely. Lower values of $\gamma$ encourage the agent to achieve reward sooner rather than later.

# Examples
To demonstrate that MDPs can encode any task, we provide some examples of complex tasks attempted by humans, and we show how they can be formalized as an MDP. The first example will show tricks that can be used to formalize complex tasks as MDPs, and the second example will show that these tricks have limits.
### Chess
We will construct an MDP representing an agent playing chess with the white pieces against an engine. Let $\mathcal S$ consist of positions in chess, along with the states $w$, $b$,  and $d$, representing a white win, black win, draw, respectively. (Note that besides $w$, $b$, and$d$, states in $\mathcal{S}$ must also include information about castling rights, en passant legality, and the recent move history to keep track of 3-fold repetition.) Let $\mathcal A$ consist of all pairs of distinct squares on the chessboard: $\mathcal A = \{(\text{a1}, \text{a2}), (\text{a1}, \text{a3}), \dots, (\text{a1}, \text{a8}), (\text{a1}, \text{b1}), \dots, (\text{a1}, \text{h8}), (\text{a2}, \text{a1}), (\text{a2}, \text{a3}) \dots\}$. For state-action pairs $(s, a)$ such that $a$ is a legal move for white in state $s$ (excluding $w$, $b$, $d$, $g$), let $s'(s, a)$ be a function that returns a state $s'$ that results when white makes the move $a$, and black makes the top engine move in response. For example, if $s_0$ is the starting state of chess, then $s'(s_0, (\text{a2},\text{a4}))$ is a position with white's a-pawn on a4, and one of black's pawns pushed (whatever the engine recommends, probably e5 or d5). We define $$\mathcal{T}(s'\mid s, a) = \begin{cases} b &\text{if }a\text{ is illegal in }s\\w & \text{if }a\text{ results in an immediate checkmate in }s\\b & \text{if the engine move causes an immediate checkmate after move }a\text{ in state }s\\d & \text{if }a\text{ results in an immediate draw}\\d & \text{if the engine move causes an immediate draw after move }a\text{ in state }s\\s &\text{if } s\in\{w, b, d\}\\s'(s, a) & \text{otherwise}\end{cases}$$So the opponent wins if we make an illegal move, and after a win, draw, or loss, we get stuck in the state $w$, $d$, or $b$ (respectively) forever afterwards. We define the reward function simply as$$r(s, a) = \begin{cases} 1 & s = w\\0 & s = d\\-1 & s = b\\0 & \text{otherwise}\end{cases}$$so after the end of the game, the agent repeatedly receives reward 1 for a win, 0 for a draw, and -1 for a loss. It does not receive any reward mid-game. Note that this means, for a win on move $t$, the discounted cumulative reward is $\frac{\gamma^t}{1-\gamma}$, meaning we receive higher reward for earlier wins (since $\gamma < 1$). Finally, our initial state distribution $\mu_0$ assigns probability 1 to the starting state $s_0$ and 0 to all other states (this could be changed to represent variants such as Chess960).

Here we have demonstrated a few of the strategies for turning complex tasks into MDPs:
- When convenient, define an overly large state space $\mathcal S$, in this case consisting of all positions in chess, even though we will only use the states which are legal with white to move.
- When legal actions differ between states, define an overly large action space $\mathcal A$, in this case consisting of all pairs of distinct squares, and handle illegal actions by assigning a negative result to the agent
- Define **absorbing states** $w, d, b$ to signify the end of the task, whether successful or not. Make these states "loop back" to themselves regardless of the action taken. This helps when an MDP could have infinite timesteps, but sometimes doesn't (e.g. chess without move number limit rules).
- Define a reward function that assigns the correct values to absorbing states. Even though the agent will receive reward for infinitely many timesteps after entering the absorbing state, the discount factor ensures that cumulative reward remains bounded.

Exercise: The MDP defined above represents chess with no limit on the number of moves. How would you define an MDP in which the game is an automatic draw after 100 moves? Can you define it as a finite-horizon MDP? An infinite-horizon MDP? Are both of these an option?

### Moon Landing
We will construct an MDP representing astronauts landing on the moon. (This example, due to complexity, will be more hand-wavy.) Let $\mathcal S$ consist of all of the possible physical states of the earth, moon, sun, spacecraft, and nearby asteroids/meteorites. A state $s\in\mathcal S$ includes information about the positions and velocities of all these objects, as well as the internal state of the spacecraft (e.g. level of thrust/acceleration from engines, status of system controls like switches). Let $\mathcal A$ consist of all possible system control changes available to the astronauts (e.g. flipping a switch, flipping both that switch and another, increasing thrust by $1 \text{m}/\text{s}^2$, increasing thrust by $.01 \text{m}/\text{s}^2$ while also flipping both switches). Let $\mathcal T(s'\mid s, a)$ be a distribution over the possible physical states 1 second after state $s$ occurs, assuming the astronauts make the system control changes corresponding to action $a$. We assume we have a powerful enough physical simulator to model all relevant considerations. Let$$r(s, a) = \begin{cases}1 &\text{the spacecraft has successfully landed in state }s\\
0&\text{the spacecraft has not successfully landed in state }s\text{, but still survives}
\\-1&\text{the spacecraft has not survived}\end{cases}$$Finally, let $\mu_0$ assign probability 1 to a pre-chosen starting state $s_0$ and probability 0 to all others. Note the following properties of the above MDP representation of this task, which were not true for the chess task:
- The state space $\mathcal S$ is continuous, since positions and velocities are
- The action space $\mathcal A$ is continuous, since some of the system controls can change continuously
Also note the following issues with the above MDP representation of this task, which did not arise in the chess task:
- We discretize time to 1 second intervals, which assumes that astronauts cannot take actions faster than this. We could change this to 1 ms, but this still fails to model autopilot systems which can take actions even faster.
- The states $s\in\mathcal S$ contain a lot of information that we probably can't measure with extreme accuracy, e.g. the positions and velocities of all nearby asteroids/meteorites.
- Even if states were measurable, the transition function $\mathcal T$ is extremely complicated due to the incorporation of multiple scales of physical phenomena. We don't have a simulator to represent $\mathcal T(s'\mid s, a)$. (Except for the real world, and using this simulator would require letting astronauts die in landing attempts!)
- Generally, in order to model everything we formally *must*, we have included a lot of information that we *can't* model, and some of it is practically irrelevant (e.g. it's very unlikely that our intended landing spot will be hit by an asteroid right before landing, changing the lunar terrain, but this possibility is included in our state space and transition function). However, it's tough to eliminate irrelevant considerations without eliminating some relevant ones as well.
This example illustrates some drawbacks of the very general MDP formulation of tasks: using it to solve real-world problems without very wisely chosen state and action spaces can introduce significant complexity. We managed to put a man on the moon without MDPs!
#### i want to figure out what i meant
We now see we have a choice as to how to interpret the discount factor. We could interpret it as a manual change in objective to provide stability in Infinite-Horizon MDPs; this is called the **Copenhagen interpretation**, after the Copenhagen interpretation of Quantum Physics, as it essentially requires accepting the discount factor without deeper explanation. We could also interpret the discount factor as representing expected total reward in a modified MDP with a death state; this is known as the **death state interpretation**. Surprisingly, these two interpretations of the discount factor have distinct real-world consequences. (?) ^5c76de


