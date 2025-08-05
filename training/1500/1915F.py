# title: 1915F.py
# author: not me
# date: 2025-08-05 19:54:18
# github: https://github.com/icekern/codeforces

import sys
from math import gcd, factorial as fact,hypot,acos,atan2,pi,ceil,sqrt,log2,isqrt,log,dist,perm,comb,prod,exp,log10,cos,sin
try: from math import lcm
except: lcm = lambda a,b: a//gcd(a,b)*b
from heapq import *
from itertools import *
try:
	from functools import cache
except:
	from functools import lru_cache
	def cache(user_function, /):
		return lru_cache(maxsize=None)(user_function)
from functools import reduce, cmp_to_key
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
from fractions import Fraction as frac
from decimal import Decimal as dec
import typing
import operator
try:
	from tqdm import trange
except:
	trange = range
from random import randint, randrange

# import pypyjit
# pypyjit.set_param(max_unroll_recursion=-1,vec=1)
# sys.setrecursionlimit(10**5+10)

input = lambda: sys.stdin.readline().strip()
def read(fn=int):
	return map(fn,input().split())
def read(*fn):
	if not fn: fn = [int]
	l = input().split()
	if len(fn) == 1: return map(fn[0], l)
	return (f(x) for f,x in zip(fn,l))

def dbg(*args,**kwargs):
	print(*args,**kwargs,file=sys.stderr)

class ostream():
	def __lshift__(self,s):
		sys.stdout.write(str(s))
		return self
cout = ostream()
endl = '\n'

yes = 'YES'
no = 'NO'

# toks = (tok for tok in sys.stdin.read().split())
# def rd(fn=int): return fn(next(toks))
# def rdn(n,fn=int): return (rd(fn) for _ in range(n))

mod = 998244353
mod = 10**9 + 7

def mul(a,b,mod=0):
	if sum(map(sum,a)) == 0 or sum(map(sum,b)) == 0:
		return [[0]*len(b[0]) for _ in range(len(a))]
	c = [[0 for j in range(len(b[0]))] for i in range(len(a))]
	for i in range(len(a)):
		for k in range(len(b)):
			for j in range(len(b[0])):
				c[i][j] += a[i][k]*b[k][j]
				if mod: c[i][j] %= mod
	return c

def power(x,y,mod=0):
	n = len(x)
	res = [[+(i==j) for j in range(n)] for i in range(n)]
	while y:
		if y % 2: res = mul(res,x,mod)
		x = mul(x,x,mod)
		y //= 2
	return res	
 
def sieve(n):
	primes = []
	isp = [1] * (n+1)
	isp[0] = isp[1] = 0
	for i in range(2,n+1):
		if isp[i]:
			primes += [i]
			for j in range(i*i,n+1,i):
				isp[j] = 0
	return primes

def eea(a,b):
	if not a: return b,0,1
	g,x,y = eea(b%a,a)
	return g, y - (b//a)*x, x

def factorials(n,mod):
	facs = [1 % mod]
	for i in range(n):
		facs += [facs[-1] * (i+1) % mod]
	invs = [pow(facs[-1], -1, mod)]
	for i in range(n):
		invs += [invs[-1] * (n-i) % mod]
	invs.reverse()
	return facs, invs

def _ceil_pow2(n):
	x = 0
	while (1 << x) < n:
		x += 1

	return x

def _bsf(n):
	x = 0
	while n % 2 == 0:
		x += 1
		n //= 2

	return x

# https://open.kattis.com/problems/mountaincraft
def solve2(case):
	q,w=read()
	l = [[*read()] for _ in range(q)]
	s={0}
	for i in range(q):
		x,y=l[i]
		l[i]=[max(x-y,0), min(x+y,w)]
		s |= {*l[i]}
	s=sorted(s)
	# print(s)
	d = {s[i]:i for i in range(len(s))}
	val = [0] * len(s)
	for i in range(len(s)-1):
		val[i] = s[i+1] - s[i]
	val[-1] = w - s[-1]
	# print(s,val)
	n = len(s)
	sz = isqrt(n)
	# print(n,sz,(n+sz-1)//sz)
	b = [0] * ((n+sz-1)//sz)
	# print(len(b), max(y//sz for _,y in l))
	f = [Counter() for _ in range((n+sz-1)//sz)]
	for i in range(len(s)):
		f[i//sz][0] += val[i]
	a = [0]*n
	seen = set()
	ans = w
	for x,y in l:
		x = d[x]
		y = d[y]
		# print(x,y)
		if (x,y) in seen:
			delta = -1
			seen.remove((x,y))
		else:
			delta = 1
			seen.add((x,y))
		
		bx = x // sz
		by = y // sz
		# print(bx,by)
		if bx == by:
			ans -= f[bx][-b[bx]]
			for i in range(x,y):
				f[bx][a[i]] -= val[i]
				a[i] += delta
				f[bx][a[i]] += val[i]
			ans += f[bx][-b[bx]]
		else:
			ans -= f[bx][-b[bx]]
			for i in range(x,(x+sz)//sz*sz):
				f[bx][a[i]] -= val[i]
				a[i] += delta
				f[bx][a[i]] += val[i]
			ans += f[bx][-b[bx]]
			
			ans -= f[by][-b[by]]
			for i in range(y//sz*sz,y):
				f[by][a[i]] -= val[i]
				a[i] += delta
				f[by][a[i]] += val[i]
			ans += f[by][-b[by]]

			for i in range(bx+1,by):
				ans -= f[i][-b[i]]
				b[i] += delta
				ans += f[i][-b[i]]
		
		# print(x,y)
		# print(bx,by)
		# print(delta)
		# print(b)
		# print(a)
		# print(f)
		# print(ans)
		print((w-ans) * 2**.5)
		# print()

def solve2(case):
	adj = []
	pre = []
	res = []
	order = []
	order_rev = []
	def ar_build(el):
		for _ in range(n):
			adj.append([])
			pre.append([])
			res.append(False)
		for i,(x,y) in enumerate(el):
			adj[x].append((y,i))
			adj[y].append((x,i))
	
	def ar_down(x, p=-1):
		# val = False
		# for y,ei in adj[x]:
		# 	if y != p:
		# 		val = val | ar_down(y,x)
		# 		pre[x].append(val)
		# return not val

		for x,p in order:
			val = False
			for y,_ in adj[x]:
				if y != p:
					val = val | (not pre[y][-1] if pre[y] else True)
					pre[x].append(val)
	
	def ar_up(x,p=-1):
		adj[x].reverse()
		for y,ei in adj[x]:
			if y == p: continue
			if pre[x]: pre[x].pop()
			res[y] = not ((res[x] or pre[x][-1]) if pre[x] else res[x])
			res[x] = res[x] or not (pre[y][-1] if pre[y] else False)
			ar_up(y,x)
		res[x] = not res[x]

		# for x,p in order_rev:

	
	def calc(el):
		ar_build(el)
		order.append((0,-1))
		order_rev.append((0,-1))
		vis = [0] * n
		vis_rev = [0] * n
		ptr = 0
		while ptr < len(order):
			v,p = order[ptr]
			vis[v] = 1
			for vv,_ in adj[v]:
				if not vis[vv]:
					order.append((vv,v))

			v,p = order_rev[ptr]
			vis_rev[v] = 1
			for vv,_ in reversed(adj[v]):
				if not vis_rev[vv]:
					order_rev.append((vv,v))

			ptr += 1
		order.reverse()
		order_rev.reverse()
		print(order)
		ar_down(0)
		ar_up(0)

	n,q = read()
	el = []
	for _ in range(n-1):
		x,y=read()
		el.append((x-1,y-1))

	calc(el)

	for x in read():
		print('Hermione' if res[x-1] else 'Ron')

def matmul(a,b,mod=0):
	c = [[0]*len(b[0]) for i in range(len(a))]
	for i in range(len(a)):
		for k in range(len(b)):
			for j in range(len(b[0])):
				c[i][j] += a[i][k]*b[k][j]
				if mod: c[i][j] %= mod
	return c

def matpowmul(x,y,v,mod=0):
	while y:
		if y % 2: v = matmul(x,v,mod)
		x = matmul(x,x,mod)
		y //= 2
	return v

def sieve(n):
	n = int(n)
	S = 10**5

	primes = []
	nsqrt = isqrt(n)
	is_prime = [1] * (nsqrt+2)
	for i in range(2,nsqrt+1):
		if is_prime[i]:
			primes += [i]
			for j in range(i*i,nsqrt+1,i):
				is_prime[j] = 0

	result = []
	block = [0] * S
	for k in range(n//S+1):
		block[:] = [1]*S
		start = k * S
		for p in primes:
			start_idx = (start + p - 1) // p
			j = max(start_idx, p) * p - start
			while j < S:
				block[j] = 0
				j += p

		if k == 0:
			block[0] = block[1] = 0
		for i in range(S):
			if start + i > n:
				break
			if block[i]:
				result += [start+i]

	return result

def polymul(a,b,mod=0):
	c = [0] * (len(a)+len(b)-1)
	for i in range(len(a)):
		for j in range(len(b)):
			c[i+j] += a[i] * b[j]
			if mod: c[i+j] %= mod
	return c

def linearRecurrence(c,s,k0,k,mod=0):
	def mul(a,b):
		ret = polymul(a,b,mod)
		for i in range(len(ret)-1,n-1,-1):
			for j in range(n-1,-1,-1):
				ret[i-j-1] += ret[i] * c[j]
				if mod: ret[i-j-1] %= mod
		return ret[:n]

	n = len(c)
	assert len(c) <= len(s)

	a = [c[0]] if n == 1 else [0,1]
	x = [1]
	k -= k0
	while k:
		if k % 2: x = mul(x,a)
		a = mul(a,a)
		k //= 2
	x = x[:n] + [0] * (n - len(x))

	ret = 0
	for i in range(n):
		ret += x[i] * s[i]
		if mod: ret %= mod
	return ret

def BM(c,s,k0,k,mod=0):
	k -= k0
	Q = [-x for x in c] + [1]
	P = polymul([-1] + s, Q, mod)[:len(Q)]
	while k:
		Qm = Q[:]
		for i in range(1,len(Q),2): Qm[i] = mod - Qm[i]
		P = polymul(P,Qm,mod)[k%2:2*(k+1):2]
		Q = polymul(Q,Qm,mod)[:2*(k+1):2]
		k //= 2
	return P[0] * pow(Q[0],-1,mod) % mod

class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1

mod=998244353
def solve(case):
	n,=read()
	l=[]
	for _ in range(n):
		a,b = read()
		l.append((a,b))
	l.sort(key=lambda x:x[1])
	
	s = sorted(x[0] for x in l)
	d = {}
	for x in s:
		d[x] = len(d)

	tree = FenwickTree([0]*n)
	ans = 0
	for a,b in l:
		ans += tree.query(n) - tree.query(d[a])
		tree.update(d[a],1)
	print(ans)

if __name__ == '__main__':
	t = 1
	# t = -1
	t, = read()
	for i in range(1,t+1):
		solve(i)