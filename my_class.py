class MyClass:
    my_list=[]
    my_dict={}
    my_set=()
    my_tuple=()

    def __init__(self) -> None:
        self.my_list=[x for x in range(200)]
        self.my_dic={d for d in range(60)}
        self.my_set=(s for s in range(400))
        self.my_tuple=(1,2,3,4,5)


    def show_list(self):
        print(self.my_list)

