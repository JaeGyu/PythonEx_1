import multiprocessing as mp 

def sq(x):
    return x * x

"""
아래의 pool구문을 위의 sq보다 위에 선언하면 에러 발생 함
url : https://stackoverflow.com/questions/36533134/cant-get-attribute-abc-on-module-main-from-abc-h-py
"""
pool = mp.Pool(processes = 2) 

if __name__ == "__main__":
    inputs = [1,2,3,4,5]
    outputs = pool.map(sq, inputs)
    print(outputs)

    outputs_async = pool.map_async(sq, inputs)
    outputs = outputs_async.get() 

    result_async = [pool.apply_async(sq,i) for i in range(100)]
    #아래처럼 하면 오류남 해결 할 것
    # print( result_async[0].get() )
    # results = [r.get() for r in result_async]
    # print(results)