def  func(*args, **kwargs):
    print(*args)
    print(args, kwargs)
    
func(1,2,3,4,5, one=0, two='yes')