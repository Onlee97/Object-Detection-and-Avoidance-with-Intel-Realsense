import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import mode1
import mode2
import mode3


def main():
	pipeline = mode2.startRsPipeline()
	mode1.main(pipeline)


if __name__ == "__main__":
	main()