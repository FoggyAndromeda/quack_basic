DECLARE FUNCTION LOGQ# (z#)
DECLARE FUNCTION SGNQ% (value!)
DECLARE FUNCTION EXPQ# (x#)
DECLARE FUNCTION SQRQ# (value#)
DECLARE FUNCTION TANQ# (x#)
DECLARE FUNCTION COSQ# (x#)
DECLARE FUNCTION SINQ# (x#)
DECLARE FUNCTION ABSOL! (value!)
'This is QBASIC library for a python interpreter
'Supported functions:
'1. ABS
'2. SIN
'3. COS
'4. TAN
'5. SQR
'6. SQN
'7. EXP
'8. LOG

FUNCTION ABS (value)
	IF value > 0 THEN
		ABS = value
	ELSE
		ABS = 0 - value
	END IF
END FUNCTION

FUNCTION COS# (x#)
	add# = 1
	res# = 0
	tempres# = res#
	ind% = 0
	WHILE (res# + add# <> tempres#)
		res# = res# + add#
		add# = add# * x# * x# * (-1) / (2 * ind% + 1) / (2 * ind% + 2)
		tempres# = res#
		ind% = ind% + 1
	WEND
	COS = res#
END FUNCTION

FUNCTION EXP# (x#)
	add# = 1
	res# = 0
	tempres# = res#
	ind% = 1
	WHILE (res# + add# <> tempres#)
		res# = res# + add#
		add# = add# * x# / ind%
		tempres# = res#
		ind% = ind% + 1
	WEND
	EXP = res#
END FUNCTION

FUNCTION LOG# (z#)
	IF z# <= 0 THEN
	       ERROR 5
	END IF
	x# = (z# - 1) / (z# + 1)
	add# = x#
	res# = 0
	tempres# = res#
	ind% = 0
	WHILE (res# + add# <> tempres#)
		res# = res# + add# / (2 * ind% + 1)
		add# = add# * x# * x#
		tempres# = res#
		ind% = ind% + 1
	WEND
	LOG = 2 * res#
END FUNCTION

FUNCTION SGN% (value)
	IF value% = 0 THEN
		SGN = 0
	END IF
	IF value% > 0 THEN
		SGN = 1
	END IF
	IF value% < 0 THEN
	       SGN = -1
	END IF
END FUNCTION

FUNCTION SIN# (x#)
	add# = x#
	res# = 0
	tempres# = res#
	ind% = 0
	WHILE (res# + add# <> tempres#)
		res# = res# + add#
		add# = add# * x# * x# * (-1) / (2 * ind% + 2) / (2 * ind% + 3)
		tempres# = res#
		ind% = ind% + 1
	WEND
	SIN = res#
END FUNCTION

FUNCTION SQR# (value#)
	IF value# = 0 THEN
		SQR = 0
	END IF
	IF value# < 0 THEN
		ERROR 5
	ELSE
		temp# = .5 * LOG(value#)
		SQR = EXP(temp#)
	END IF
END FUNCTION

FUNCTION TANQ# (x#)
	TANQ = SIN(x#) / COS(x#)
END FUNCTION

