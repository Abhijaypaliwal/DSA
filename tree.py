'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []
        
    def addChild(self,child):
        child.parent = self
        self.children.append(child)
    
    def printTree(self):
        print(self.data)
        
        for child in self.children:
            print("|__",child.data)
            for furtherChild in child.children:
                print("  |__",furtherChild.data)

def build_product_tree():
    root = TreeNode("electronics")
    laptop = TreeNode("Laptop")
    root.addChild(laptop)
    laptop.addChild(TreeNode("Macbook"))
    laptop.addChild(TreeNode("dell"))
    laptop.addChild(TreeNode("lenovo"))
    cellphone = TreeNode("smartphone")
    cellphone.addChild(TreeNode("apple"))
    cellphone.addChild(TreeNode("ONEPLUS"))
    cellphone.addChild(TreeNode("vivo"))
    TV = TreeNode("Television")
    TV.addChild(TreeNode("lg"))
    TV.addChild(TreeNode("samsung"))
    root.addChild(cellphone)
    root.addChild(TV)
    return root
    
if __name__ == '__main__':
    root = build_product_tree()
    root.printTree()
    print("hel")
    #print(root)
        
