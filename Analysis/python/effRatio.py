import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%
# parse file

#with open('out.txt') as f:
#    lines = f.read().splitlines()
#f = open('dataOrig.txt')
f = open('dataMore.txt') # read file
lines = f.readlines()    # parse line by line
x = []
y = []
z = []

for i in range(len(lines)):
    dummylist = lines[i].split(' ')
    x.append(dummylist[0])
    y.append(dummylist[len(dummylist)-2])
#    z.append(dummylist[len(dummylist)-1])

r = open('ratio.txt')
ratios = r.readlines()
for i in range(len(ratios)):
    dummylist = ratios[i].split(' ')
    z.append(dummylist[len(dummylist)-1])
    
#print(lines[i])
#print(x)
#print(y)

# remove '-'
for i in range(len(x)):
    x[i] = x[i].split('-',1)[0]

# remove '>'
for i in range(len(x)):
    if ('>' in x[i]):
        x[i] = x[i][1:]
print(x)
print(y) # nothing to remove

# remove '\n'
for i in range(len(z)):
    z[i] = z[i][:-1]
print(z)

#%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%
# plot

# remove double counting the pt (since we have both fast and full)
plotx = []
for i in range(len(x)/2):
    plotx.append(x[i])
print(plotx)

# calculate the ratio
ploty = []
for i in range(len(y)/2):
    ploty.append(float(y[i])/float(y[i+(len(y))/2]))
print(ploty)

# calculate/average error bars
plotz = []
for i in range(len(z)):
    plotz.append(float(z[i]))
#for i in range(len(z)/2):
#    plotz.append((float(z[i])+float(z[i+(len(z))/2]))/2)
print(plotz)

plt.scatter(plotx, ploty)
plt.errorbar(plotx, ploty, yerr=plotz, ls='none')
#plt.plot(plotx, ploty)
one = []
for i in range(len(plotx)):
    one.append(1)
plt.plot(plotx, one)

plt.xlabel('p_T [GeV]')
plt.ylabel('Fast/Full')
plt.title('deepTagMD_HbbvsQCD_eff Fast/Full vs p_T')
plt.savefig('deepTagMD_HbbvsQCD_eff.png')

# y = []
# for i, eff in enumerate(efficiencies):
#   y.append(eff.val)
# 
# #f = plt.figure()
# plt.scatter(pt_thresholds, y)
# plt.xlabel('pt [GeV]')
# plt.ylabel('efficiency/100 GeV')
# simType = 'FullSim' if not options.fastSim else 'FastSim'
# plt.title('efficiency vs pt ' + simType)
# plt.savefig(simType + '.png')
# #plt.show()
# #f.savefig("out.pdf")
