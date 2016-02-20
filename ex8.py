#_*_ coding: utf-8 _*_

formatter = "%s %s %s %s"

print formatter % (1,2,3,4)
print formatter % (formatter,formatter,formatter,formatter)

formatter2 = "%r %r %r %r"
print formatter2 % (
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing",
	"Do I said goodnight"
)

print formatter2 % (True,False,True,False)
print formatter2 % ("한","재","규","다")
