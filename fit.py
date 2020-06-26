import numpy as np
import matplotlib.pyplot as plt
from run import run_solution

"""
lg_ = np.array([np.log(x) for x in list(range(1,100))])
lg_abs = np.sum(lg_)
lin_ = np.arange(1,100)
lin_abs = np.sum(lin_)

m,c = np.polyfit(lin_,lg_,1)
plt.plot(lin_,lg_)

reg_ = np.array(list(map(lambda x: m*x+c, lin_)))
plt.plot(lin_,reg_)
plt.show()
"""
# print(np.correlate(lg_,lin_)/lg_abs/lin_abs)
# print(np.correlate(lin_,lin_)/lin_abs/lin_abs)


def check_fits(solution_name, problem_maker_name, max=1000, verbose=False):
    lin = np.arange(1, max, max / 100)
    cons = np.full(lin.shape, 1)
    lg = np.array(list(map(lambda x: np.log(x), lin)))
    linarith = np.array(list(map(lambda x: np.log(x) * x, lin)))
    sq = np.array(list(map(lambda x: x ** 2, lin)))
    cub = np.array(list(map(lambda x: x ** 3, lin)))

    plt.plot(lin, np.log(cons), label="O(k)")
    plt.plot(lin, np.log(lg), label="O(lg(n))")
    plt.plot(lin, np.log(lin), label="O(n)")
    plt.plot(lin, np.log(linarith), label="O(nlg(n))")
    plt.plot(lin, np.log(sq), label="O(n^2)")
    plt.plot(lin, np.log(cub), label="O(n^3)")

    soln = np.array(
        list(
            map(
                lambda x: run_solution(solution_name, problem_maker_name, x),
                lin,
            )
        )
    )

    plt.plot(lin, np.log(soln), label="Solution")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    check_fits(
        "problem_soln_pairs/linear_soln", "problem_soln_pairs/linear_maker"
    )
