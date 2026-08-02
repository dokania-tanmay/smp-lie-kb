# Purpose and Structure
The objective of this repository is to learn and prove probabilistic tube guaranttees for Riemannian manifolds/Lie groups. As this is a non-trivial effort, where a lot of math needs to be learned by me, I desire Claude to help me learn the requiste math so that I can step-by-step verify and develop good insights into the problem.
The best way to learn a new math topic is solve problems and try to prove simple theorems by recalling definitions. Therefore, I want Claude to create a learning pathway for the concepts I don't understand that includes key definitions, simple theorems and corollaries. Also, simple problems that I can solve 

Keep the source references in `refs` which contains the source papers and a markdown version with everything rewritten so that it can be retrieved by Claude easily without wasting tokens again.

In `notes`, I desire to create notes on my own from the content I read and understand, so I want to keep them in a different folder.

In `tools`, I want to keep the python scripts that are used to retrieve the source latex files from arxiv files and blogs from different websites. 

In `content`, I desire to Claude to generate reading material with practice problems tailored for the problem statement at hand.

# Pathway
Lets restrict the analysis to matrix Lie groups. Then, we can loosen up to homogeneous manifolds and then ultimately Riemannian manifolds. Given Lie groups have a lot of structure, some them can be conflicting, such as the definition of the Log map can be obtained from a metric on a manifold and can also be obtained through flows of left invariant vector fields. We will stick to simplifying assumptions and present the key ideas.
*Focus: Coordinate-based treatment of **intrinsic** objects.*

1. Derive Hamiltonian Dynamics on Lie groups
2. Consider a simple class of tracking controllers with stabilizing properties (contraction?)
3. Introduce Brownian Noise in forces/torque terms and construct the Generator for both controlled and uncontrolled systems
4. Define a distance-function that is coordinate-invariant on the Lie group, inspired from the AMGF function
5. Operate the generator to show that the function is a martingale
6. Formulate a deterministic surrogate of a trajectory optimization problem on a manifold

# Potential Results
- Curvature of the tangent components in the Sasaki metric
- Contraction theory for Hamiltonian system on Lie groups, by introducing a coupling term in metric from hierarchical contraction
- Coordinate invariance as noise enters on the flat subsystem
- A general tube function based on the curvature/Laplacian, which is either lower or upper bounded
- No curvature correction terms as noise is entering in flat subsystem