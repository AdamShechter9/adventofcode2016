# Adam Shechter
# Solving for adventofcode challenge, day1 part 1
# Using input1.txt as data
# my solution uses an array of hash tables representing coordinates.
# this array gets scanned for previous coordinate to match current coordinate.
# if not, then traveled coordinate is added.

# an alternate solution is to create a multidimensional grid (matrix)
# and initialize with 0's.  set to 1 when traveled to coordinate.
# run a check to find first double-visited coordinate.


import sys

DIRECTIONS = ['N', 'E', 'S', 'W']

class day1solution(object):
	def __init__(self):
		self.direction = 0
		self.coordinate = {'x': 0, 'y': 0}

	def move(self, inp1):
		newDirect = inp1[0:1]
		newSteps = int(inp1[1:])
		#print(newDirect+" "+str(newSteps))
		if newDirect == 'R':
			if (self.direction + 1) > 3:
				self.direction = 0
			else:
				self.direction+=1
		elif newDirect == 'L':
			if (self.direction - 1) < 0:
				self.direction = 3
			else:
				self.direction-=1
		else:
			raise "Error: incorrect input"

		if self.direction == 0:
			# N
			self.coordinate['y']+=newSteps
		elif self.direction == 1:
			# E
			self.coordinate['x']+=newSteps
		elif self.direction == 2:
			# S
			self.coordinate['y']-=newSteps
		elif self.direction == 3:
			# W
			self.coordinate['x']-=newSteps

		return self.coordinate

class day2solution(object):
	def __init__(self):
		self.direction = 0
		self.coordinate = {'x': 0, 'y': 0}
		self.map = [{'x': 0, 'y': 0}]

	def move(self, inp1):
		def scanMap(self, coord1):
			# list search
			foundCoord = False
			for coord1 in self.map:
				#print("testing coord "+str(coord1)+" against self location "+str(self.coordinate))
				if coord1['x'] == self.coordinate['x'] and coord1['y'] == self.coordinate['y']:
					foundCoord = True
			return foundCoord

		newDirect = inp1[0:1]
		newSteps = int(inp1[1:])
		#print(newDirect+" "+str(newSteps))

		#Set direction
		if newDirect == 'R':
			if (self.direction + 1) > 3:
				self.direction = 0
			else:
				self.direction+=1
		elif newDirect == 'L':
			if (self.direction - 1) < 0:
				self.direction = 3
			else:
				self.direction-=1
		else:
			raise "Error: incorrect input"

		#move coordinate and populate map
		if self.direction == 0:
			# N
			for step in range(newSteps):
				self.coordinate['y']+=1
				currCoord = {'x':self.coordinate['x'], 'y':self.coordinate['y']}
				found = scanMap(self, currCoord)
				if not found:
					self.map.append(currCoord)
				else:
					print ("LOCATION FOUND")
					return -1

		elif self.direction == 1:
			# E
			for step in range(newSteps):
				self.coordinate['x']+=1
				currCoord = {'x':self.coordinate['x'], 'y':self.coordinate['y']}
				found = scanMap(self, currCoord)
				if not found:
					self.map.append(currCoord)
				else:
					print ("LOCATION FOUND")
					return -1
		elif self.direction == 2:
			# S
			for step in range(newSteps):
				self.coordinate['y']-=1
				currCoord = {'x':self.coordinate['x'], 'y':self.coordinate['y']}
				found = scanMap(self, currCoord)
				if not found:
					self.map.append(currCoord)
				else:
					print ("LOCATION FOUND")
					return -1

		elif self.direction == 3:
			# W
			for step in range(newSteps):
				self.coordinate['x']-=1
				currCoord = {'x':self.coordinate['x'], 'y':self.coordinate['y']}
				found = scanMap(self, currCoord)
				if not found:
					self.map.append(currCoord)
				else:
					print ("LOCATION FOUND")
					return -1


		return "complete running.  no intersection"

def main():
	test1 = "R1, R1, R3, R1, R1, L2"
	graph1 = day1solution()
	graph2 = day2solution()
	with open('input1.txt', 'r') as f:
		test2 = f.readline().strip().split(', ')

	#currDirections = test1.split(', ')
	currDirections = test2

	#print(currDirections)
	for inst1 in currDirections:
		print("Instruction: "+inst1)
		#print(graph1.move(inst1))
		result = graph2.move(inst1)
		if result != -1:
			print(result)
		else:
			print ("FOUND")
			break

	return graph2.coordinate

print(main())
