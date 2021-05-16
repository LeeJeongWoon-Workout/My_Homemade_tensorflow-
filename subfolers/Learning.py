for epoch in range(epochs):
  if epoch%4==0:
    lr=0.9*lr
  for idx in range(len(x_data)):
    x,y=x_data[idx],y_data[idx]

    z1=node1.forward(th,x)
    z2=node2.forward(y,z1)
    z3=node3.forward(z2)

    dz2=node3.backward(1)
    dy,dz1=node2.backward(dz2)
    dth,dx=node1.backward(dz1)

    th=th-lr*dth

    loss_list.append(z3)
    th_list.append(th)
