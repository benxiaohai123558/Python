tup = ()  # 创建空元组
print(tup)

tup1 = ("a", "b", "c")
tup2 = "x", "y", 'z'  # 不需要括号也可以
print(tup1)
print(tup2)

tup3 = (1)  # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
print(type(tup3))  ## 不加逗号，类型为整型
tup4 = (1,)
print(type(tup4))

# ---- 访问元组 ----
print(tup1[0])  # 元组可以使用下标索引来访问元组中的值
print(tup1[1:3])

# ---- 修改元组 ----
# tup1[0] = 100 #以下修改元组元素操作是非法的
print(tup1 + tup2)  # 元组进行连接组合

# ---- 删除元组 ----
del tup4  # 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
# print(tup4)  # 删除之后不能访问
