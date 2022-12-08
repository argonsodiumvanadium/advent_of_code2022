class TreeNode():
    def __init__ (self,name, parent=None, space=-1, children=None):
        self.children = children
        self.parent = parent
        self.space=space
        self.name=name

    def __str__ (self):
        return f'< treenode {self.name}>'

    def load (self, fname):
        lines=open(fname).read().split('\n')[1:-1]
        itr=self
        readmode=False
        for line in lines:
            if readmode and line[0] == '$':
                readmode=False
            if readmode:
                itr.add_child(line)
            if line.split(' ')[1] == 'cd':
                if line.split(' ')[2] == '..':
                    itr=itr.parent
                    continue
                itr=itr.children[line.split(' ')[2]]
            if line.split(' ')[1] == 'ls':
                readmode=True
    
    def add_child(self, line):
        words = line.split(' ')
        if words[0] == 'dir':
            self.children[words[1]]=TreeNode(words[1],parent=self,children={})
        else:
            self.children[words[1]]=TreeNode(words[1],self,int(words[0]),None)

    def evaluate_space(self):
        if self.children==None:
            return self.space
        else:
            _sum=0
            for key,item in self.children.items():
                _sum += item.evaluate_space()
            self.space=_sum
            return _sum

    def PART_1_find_desired_directories(self):
        arr = [] 
        if self.children==None:
            return []
        else:
            for key, item in self.children.items():
                if item.space <= 100000 and item.children:
                    arr.append(item.space)
                if item.children:
                    for i in item.PART_1_find_desired_directories():
                        arr.append(i)
            return arr


    def PART_2_find_desired_directories(self,required_space):
        arr = [] 
        if self.children==None:
            return []
        else:
            for key, item in self.children.items():
                if item.space >= required_space and item.children:
                    arr.append(item.space)
                if item.children:
                    for i in item.PART_2_find_desired_directories(required_space):
                        arr.append(i)
            return arr

def main():
    tree=TreeNode('/',children={})
    tree.load('input.in')
    tree.evaluate_space()
    print('part 1 :',sum(tree.PART_1_find_desired_directories()))

    print(tree.space)
    freespace = 70000000-tree.space
    required_space=30000000-freespace
    print('part 2 :',min(tree.PART_2_find_desired_directories(required_space)))

main()
