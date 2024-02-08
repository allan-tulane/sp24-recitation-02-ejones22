from main import *
import math

def test_simple_work():
  """ done. """
  assert simple_work_calc(15, 3, 5) == 24
  assert simple_work_calc(25, 2, 3) == 49
  assert simple_work_calc(50, 1, 5) == 62
  assert simple_work_calc(10, 2, 10) == 12
  
  

def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(100, 1, 2, lambda n: n) == 197
  assert work_calc(25, 1, 4, lambda n: n*n) == 662

def test_compare_work():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work
    
  # create work_fn1
  def work_fn1(n):
    a = 16
    b = 2
    c = 6
    f = lambda n:math.pow(n,c) # n^c
    return work_calc(n, a, b, f)
    
  # create work_fn2
  def work_fn2(n):
    a = 16
    b = 2
    c = 6
    f = lambda n:math.pow(n,c)
    return work_calc(n, a, b, f)

  res = compare_work(work_fn1, work_fn2)
  #print("compare_work results" , res)
  return ("compare_work results" , res)
  

def test_compare_span():
  def span_fn1(n):
    a = 16
    b = 2
    f = lambda n: 1
    return span_calc(n, a, b, f)

  def span_fn2(n):
    a = 16
    b = 2
    f = lambda n: math.log(n)
    return span_calc(n, a, b, f)

  def span_fn3(n):
    a = 16
    b = 2
    f = lambda n: n
    return span_calc(n, a, b, f)
  res = compare_span(span_fn1, span_fn2)
  
  return ("compare_span results" , res)
