def toh(n, src, aux1, aux2, dest):
    if n==0:
        return
    elif n==1:
        print(f"move disk {n} from {src} to {dest}")
        return
    else:
        #move the n-2 towers to the aux2 by using aux1
        toh(n-2,src, aux1, dest, aux2)

        #then move the (n-1)th tower to the aux1
        print(f"move disk {n-1} from {src} to {aux1}")

        #then move the (n)th tower to the dest
        print(f"move disk {n} from {src} to {dest}")

        #then move the (n-1)th tower to the dest
        print(f"move disk {n-1} from {aux1} to {dest}")

        #then move the n-2 towers to the dest by using aux1
        toh(n-2,aux2, aux1, src, dest)
    
    return

toh(5,"peg1","peg2","peg3","peg4")
