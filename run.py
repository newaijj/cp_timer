from timeit import timeit
from io import StringIO
import os
import subprocess
import logging
from logging import info

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def run_solution(solution_name, problem_maker_name, generator_input,verbose=False):

	with open("generator_input.txt","w") as g_i:
		g_i.write(generator_input)
		g_i.flush()

	with open("generator_input.txt","r") as g_i:
		with open("input.txt","w") as f_i:
			problem_maker_path = os.getcwd() +'/'+ problem_maker_name
			subprocess.run(problem_maker_path,stdin=g_i,stdout=f_i)


	solution_path = os.getcwd() +'/'+ solution_name
	with open("input.txt","r") as f_i:
		with open("out.txt","w") as f_o:
			time = timeit(stmt = "subprocess.run( solution_path ,stdin = f_i, stdout = f_o)", setup = "import subprocess", number = 1,globals={"solution_path":solution_path,"f_i":f_i,"f_o":f_o})
	if verbose:
		with open("out.txt","r") as ans:
			info("{} tested on {} with input {}".format(solution_name,problem_maker_name,generator_input))
			info("Completed in {}s".format(time))

	

	os.remove("generator_input.txt")
	os.remove("input.txt")
	os.remove("out.txt")

	return time

run_solution("cpp","problem_maker","5",verbose=True)