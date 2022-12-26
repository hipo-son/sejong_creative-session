import numpy as np
import matplotlib.pyplot as plt

path="/Users/yararal/1code/downloads_slurm/Si_re_pro/datafile/logs/"
titles=["30-30, 5000, 0.003",       #1
        "30-30, 5000, 0.003, 0.5",  #2
        "30-30, 5000, 0.0001",      #3
        "10-10, 5000, 0.003",       #4
        "30-30, 10000, 0.003, 0.2", #5
        "25-25, 10000, 0.003, 0.2", #6
        "15-15, 10000, 0.003, 0.05",#7
        "10-10, 5000, 0.0001",      #8
        ]


z=0
while z<len(titles):

    step,E_RMSE_T,E_RMSE_v,F_RMSE_T,F_RMSE_v=[],[],[],[],[]

    with open(path+f'LOG_{z+1}') as t:
        data=t.readlines()
    # print(data)
    h=0
    while h<len(data):
        asd=data[h].split()
        step.append(float(asd[1]))
        E_RMSE_T.append(float(asd[5]))
        E_RMSE_v.append(float(asd[6]))
        F_RMSE_T.append(float(asd[10]))
        F_RMSE_v.append(float(asd[11]))
        h+=1

    # data=np.loadtxt()
    # data=data.T
    # step, E_t, E_v, F_t, F_v=data

    E_RMSE_T, E_RMSE_v=np.log10(E_RMSE_T), np.log10(E_RMSE_v)
    
    # plt.plot(step, E_RMSE_T, alpha=.3, label="RMSE train")
    # plt.plot(step, E_RMSE_v, alpha=.3, label="RMSE vaild")
    plt.plot(step, E_RMSE_v, alpha=.3, label=f"RMSE vaild_{z+1}")
    plt.ylim([0,1])
    plt.ylim([-3,-1])
    # plt.xlim([0,5000])
    plt.xlabel("Epoch")
    plt.ylabel("RMSE")
    plt.title(f"{z+1}: "+titles[z])
    plt.legend()
    # plt.show()
    plt.savefig(f"첨부 자료/RMSE_E_{z+1}.png" )
    # plt.cla()
    z+=1



# path="/Users/yararal/1code/downloads_slurm/Si_re_pro/datafile/total_e.dat"

# with open(path) as t:
#     data=t.readlines()
# del data[0]

# step,energy= [],[]
# z=0
# while z<len(data):
#     asd=data[z].split()
#     step.append(float(asd[1]))
#     energy.append(float(asd[4]))
#     z+=1

# plt.plot(step,energy)
# plt.savefig(f"첨부 자료/MD_energy.png" )
# plt.show()


