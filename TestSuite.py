"""
Author: NTM - 4/22/2025
Test case:
    INSERT:      0 ->  59:  60
    ASSIGN:     60 -> 175: 116
    BEGIN+END: 176 -> 276: 101
    LOOKUP:    277 -> 332:  56
    PRINT:     333 -> 359:  27
    RPRINT:    360 -> 386:  27
    OTHER:     387 -> 399:  13
    ...
    Total:     0   -> 399: 400
"""

import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):

    """======================================================INSERT======================================================"""
    def test_0(self):
        input = ["INSERT a number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10000))

    def test_1(self):
        input = ["INSERT a string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10001))

    def test_2(self):
        input = ["INSERT b2 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10002))

    def test_3(self):
        input = ["INSERT b2 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10003))

    def test_4(self):
        input = ["INSERT bE2 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10004))

    def test_5(self):
        input = ["INSERT bE2 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10005))

    def test_6(self):
        input = ["INSERT bE_2 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10006))

    def test_7(self):
        input = ["INSERT bE_2 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10007))

    def test_8(self):
        input = ["INSERT b_ number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10008))

    def test_9(self):
        input = ["INSERT b_ string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10009))

    def test_10(self):
        input = ["INSERT b2_ number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10010))

    def test_11(self):
        input = ["INSERT b2_ string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10011))

    def test_12(self):
        input = ["INSERT string string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10012))

    def test_13(self):
        input = ["INSERT string number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10013))

    def test_14(self):
        input = ["INSERT number string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10014))

    def test_15(self):
        input = ["INSERT number number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10015))
      
    def test_16(self):
        input = ["INSERT B string"]
        expected = ["Invalid: INSERT B string"]
        self.assertTrue(TestUtils.check(input, expected, 10016))

    def test_17(self):
        input = ["INSERT B number"]
        expected = ["Invalid: INSERT B number"]
        self.assertTrue(TestUtils.check(input, expected, 10017))

    def test_18(self):
        input = ["INSERT Ba string"]
        expected = ["Invalid: INSERT Ba string"]
        self.assertTrue(TestUtils.check(input, expected, 10018))

    def test_19(self):
        input = ["INSERT Ba number"]
        expected = ["Invalid: INSERT Ba number"]
        self.assertTrue(TestUtils.check(input, expected, 10019))

    def test_20(self):
        input = ["INSERT B2 string"]
        expected = ["Invalid: INSERT B2 string"]
        self.assertTrue(TestUtils.check(input, expected, 10020))

    def test_21(self):
        input = ["INSERT B2 number"]
        expected = ["Invalid: INSERT B2 number"]
        self.assertTrue(TestUtils.check(input, expected, 10021))

    def test_22(self):
        input = ["INSERT _ string"]
        expected = ["Invalid: INSERT _ string"]
        self.assertTrue(TestUtils.check(input, expected, 10022))

    def test_23(self):
        input = ["INSERT _ number"]
        expected = ["Invalid: INSERT _ number"]
        self.assertTrue(TestUtils.check(input, expected, 10023))

    def test_24(self):
        input = ["INSERT _b string"]
        expected = ["Invalid: INSERT _b string"]
        self.assertTrue(TestUtils.check(input, expected, 10024))

    def test_25(self):
        input = ["INSERT _b number"]
        expected = ["Invalid: INSERT _b number"]
        self.assertTrue(TestUtils.check(input, expected, 10025))

    def test_26(self):
        input = ["INSERT 3e string"]
        expected = ["Invalid: INSERT 3e string"]
        self.assertTrue(TestUtils.check(input, expected, 10026))

    def test_27(self):
        input = ["INSERT 3e number"]
        expected = ["Invalid: INSERT 3e number"]
        self.assertTrue(TestUtils.check(input, expected, 10027))

    def test_28(self):
        input = ["INSERT azAZ09_ string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10028))

    def test_29(self):
        input = ["INSERT azAZ09_ number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10029))

    def test_30(self):
        input = [" INSERT abc string"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10030))

    def test_31(self):
        input = ["INSERT  abc string"]
        expected = ["Invalid: INSERT  abc string"]
        self.assertTrue(TestUtils.check(input, expected, 10031))

    def test_32(self):
        input = ["INSERT abc  string"]
        expected = ["Invalid: INSERT abc  string"]
        self.assertTrue(TestUtils.check(input, expected, 10032))

    def test_33(self):
        input = ["INSERT abc string "]
        expected = ["Invalid: INSERT abc string "]
        self.assertTrue(TestUtils.check(input, expected, 10033))

    def test_34(self):
        input = ["INSERT abc string number"]
        expected = ["Invalid: INSERT abc string number"]
        self.assertTrue(TestUtils.check(input, expected, 10034))

    def test_35(self):
        input = ["INSERT bc ed string"]
        expected = ["Invalid: INSERT bc ed string"]
        self.assertTrue(TestUtils.check(input, expected, 10035))

    def test_36(self):
        input = ["INSERT bc@ed number"]
        expected = ["Invalid: INSERT bc@ed number"]
        self.assertTrue(TestUtils.check(input, expected, 10036))

    def test_37(self):
        input = ["INSERT bc@ed string"]
        expected = ["Invalid: INSERT bc@ed string"]
        self.assertTrue(TestUtils.check(input, expected, 10037))

    def test_38(self):
        input = ["INSERT bc`ed number"]
        expected = ["Invalid: INSERT bc`ed number"]
        self.assertTrue(TestUtils.check(input, expected, 10038))

    def test_39(self):
        input = ["INSERT bc`ed string"]
        expected = ["Invalid: INSERT bc`ed string"]
        self.assertTrue(TestUtils.check(input, expected, 10039))

    def test_40(self):
        input = ["INSERT bc~ed number"]
        expected = ["Invalid: INSERT bc~ed number"]
        self.assertTrue(TestUtils.check(input, expected, 10040))

    def test_41(self):
        input = ["INSERT bc~ed string"]
        expected = ["Invalid: INSERT bc~ed string"]
        self.assertTrue(TestUtils.check(input, expected, 10041))

    def test_42(self):
        input = ["INSERT bced Number"]
        expected = ["Invalid: INSERT bced Number"]
        self.assertTrue(TestUtils.check(input, expected, 10042))

    def test_43(self):
        input = ["INSERT bced String"]
        expected = ["Invalid: INSERT bced String"]
        self.assertTrue(TestUtils.check(input, expected, 10043))

    def test_44(self):
        input = ["INSERT bced nuMber"]
        expected = ["Invalid: INSERT bced nuMber"]
        self.assertTrue(TestUtils.check(input, expected, 10044))

    def test_45(self):
        input = ["INSERT bced stRing"]
        expected = ["Invalid: INSERT bced stRing"]
        self.assertTrue(TestUtils.check(input, expected, 10045))

    def test_46(self):
        input = ["INSERT bced "]
        expected = ["Invalid: INSERT bced "]
        self.assertTrue(TestUtils.check(input, expected, 10046))

    def test_47(self):
        input = ["INSERT bced"]
        expected = ["Invalid: INSERT bced"]
        self.assertTrue(TestUtils.check(input, expected, 10047))

    def test_48(self):
        input = ["INSERT string bced"]
        expected = ["Invalid: INSERT string bced"]
        self.assertTrue(TestUtils.check(input, expected, 10048))

    def test_49(self):
        input = ["INSERT number bced"]
        expected = ["Invalid: INSERT number bced"]
        self.assertTrue(TestUtils.check(input, expected, 10049))

    def test_50(self):
        input = ["INSERT  string"]
        expected = ["Invalid: INSERT  string"]
        self.assertTrue(TestUtils.check(input, expected, 10050))

    def test_51(self):
        input = ["INSERT  number"]
        expected = ["Invalid: INSERT  number"]
        self.assertTrue(TestUtils.check(input, expected, 10051))

    def test_52(self):
        input = ["INSERT  "]
        expected = ["Invalid: INSERT  "]
        self.assertTrue(TestUtils.check(input, expected, 10052))

    def test_53(self):
        input = ["INSERT "]
        expected = ["Invalid: INSERT "]
        self.assertTrue(TestUtils.check(input, expected, 10053))

    def test_54(self):
        input = ["INSERT"]
        expected = ["Invalid: INSERT"]
        self.assertTrue(TestUtils.check(input, expected, 10054))

    def test_55(self):
        input = ["INSERT abc number", "INSERT abcd string"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10055))

    def test_56(self):
        input = ["INSERT abc number", "INSERT abc number"]
        expected = ["Redeclared: INSERT abc number"]
        self.assertTrue(TestUtils.check(input, expected, 10056))

    def test_57(self):
        input = ["INSERT abc number", "INSERT abc string"]
        expected = ["Redeclared: INSERT abc string"]
        self.assertTrue(TestUtils.check(input, expected, 10057))

    def test_58(self):
        input = ["INSERT abc number", "INSERT abcd number", "INSERT abc number"]
        expected = ["Redeclared: INSERT abc number"]
        self.assertTrue(TestUtils.check(input, expected, 10058))

    def test_59(self):
        input = ["INSERT abcde number", "INSERT abc number", "INSERT abcd number", "INSERT abcdef number", "INSERT abc number", "INSERT abcde number"]
        expected = ["Redeclared: INSERT abc number"]
        self.assertTrue(TestUtils.check(input, expected, 10059))

    """======================================================ASSIGN======================================================"""

    def test_60(self):
        input = ["INSERT x number", "ASSIGN x 1"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10060))

    def test_61(self):
        input = ["INSERT x number", "ASSIGN x 12"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10061))

    def test_62(self):
        input = ["INSERT x number", "ASSIGN x 123"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10062))

    def test_63(self):
        input = ["INSERT x number", "ASSIGN x 12.2"]
        expected = ["Invalid: ASSIGN x 12.2"]
        self.assertTrue(TestUtils.check(input, expected, 10063))

    def test_64(self):
        input = ["INSERT x number", "ASSIGN x -122"]
        expected = ["Invalid: ASSIGN x -122"]
        self.assertTrue(TestUtils.check(input, expected, 10064))

    def test_65(self):
        input = ["INSERT x string", "ASSIGN x 'a'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10065))

    def test_66(self):
        input = ["INSERT x string", "ASSIGN x '1'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10066))

    def test_67(self):
        input = ["INSERT x string", "ASSIGN x '1bc'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10067))

    def test_68(self):
        input = ["INSERT x string", "ASSIGN x '1bC'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10068))

    def test_69(self):
        input = ["INSERT x string", "ASSIGN x 'azAZ09'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10069))

    def test_70(self):
        input = ["INSERT x string", "ASSIGN x 'a_a'"]
        expected = ["Invalid: ASSIGN x 'a_a'"]
        self.assertTrue(TestUtils.check(input, expected, 10070))

    def test_71(self):
        input = ["INSERT x string", "ASSIGN x 'a@a'"]
        expected = ["Invalid: ASSIGN x 'a@a'"]
        self.assertTrue(TestUtils.check(input, expected, 10071))

    def test_72(self):
        input = ["INSERT x string", "ASSIGN x 'a`a'"]
        expected = ["Invalid: ASSIGN x 'a`a'"]
        self.assertTrue(TestUtils.check(input, expected, 10072))

    def test_73(self):
        input = ["INSERT x string", "ASSIGN x 'a~a'"]
        expected = ["Invalid: ASSIGN x 'a~a'"]
        self.assertTrue(TestUtils.check(input, expected, 10073))

    def test_74(self):
        input = ["INSERT x string", "ASSIGN x 'a~a'"]
        expected = ["Invalid: ASSIGN x 'a~a'"]
        self.assertTrue(TestUtils.check(input, expected, 10074))

    def test_75(self):
        input = ["INSERT x string", "ASSIGN x 'a a'"]
        expected = ["Invalid: ASSIGN x 'a a'"]
        self.assertTrue(TestUtils.check(input, expected, 10075))

    def test_76(self):
        input = ["ASSIGN B 1"]
        expected = ["Invalid: ASSIGN B 1"]
        self.assertTrue(TestUtils.check(input, expected, 10076))

    def test_77(self):
        input = ["ASSIGN Ba 1"]
        expected = ["Invalid: ASSIGN Ba 1"]
        self.assertTrue(TestUtils.check(input, expected, 10077))

    def test_78(self):
        input = ["ASSIGN B2 1"]
        expected = ["Invalid: ASSIGN B2 1"]
        self.assertTrue(TestUtils.check(input, expected, 10078))

    def test_79(self):
        input = ["ASSIGN _ 1"]
        expected = ["Invalid: ASSIGN _ 1"]
        self.assertTrue(TestUtils.check(input, expected, 10079))

    def test_80(self):
        input = ["ASSIGN _b 1"]
        expected = ["Invalid: ASSIGN _b 1"]
        self.assertTrue(TestUtils.check(input, expected, 10080))

    def test_81(self):
        input = ["ASSIGN 3e 1"]
        expected = ["Invalid: ASSIGN 3e 1"]
        self.assertTrue(TestUtils.check(input, expected, 10081))

    def test_82(self):
        input = ["ASSIGN bc@ed 1"]
        expected = ["Invalid: ASSIGN bc@ed 1"]
        self.assertTrue(TestUtils.check(input, expected, 10082))

    def test_83(self):
        input = ["ASSIGN bc`ed 1"]
        expected = ["Invalid: ASSIGN bc`ed 1"]
        self.assertTrue(TestUtils.check(input, expected, 10083))

    def test_84(self):
        input = ["ASSIGN bc~ed 1"]
        expected = ["Invalid: ASSIGN bc~ed 1"]
        self.assertTrue(TestUtils.check(input, expected, 10084))

    def test_85(self):
        input = ["INSERT x string", "ASSIGN x B"]
        expected = ["Invalid: ASSIGN x B"]
        self.assertTrue(TestUtils.check(input, expected, 10085))

    def test_86(self):
        input = ["INSERT x number", "ASSIGN x B"]
        expected = ["Invalid: ASSIGN x B"]
        self.assertTrue(TestUtils.check(input, expected, 10086))

    def test_87(self):
        input = ["INSERT x string", "ASSIGN x Ba"]
        expected = ["Invalid: ASSIGN x Ba"]
        self.assertTrue(TestUtils.check(input, expected, 10087))

    def test_88(self):
        input = ["INSERT x number", "ASSIGN x Ba"]
        expected = ["Invalid: ASSIGN x Ba"]
        self.assertTrue(TestUtils.check(input, expected, 10088))

    def test_89(self):
        input = ["INSERT x string", "ASSIGN x B2"]
        expected = ["Invalid: ASSIGN x B2"]
        self.assertTrue(TestUtils.check(input, expected, 10089))

    def test_90(self):
        input = ["INSERT x number", "ASSIGN x B2"]
        expected = ["Invalid: ASSIGN x B2"]
        self.assertTrue(TestUtils.check(input, expected, 10090))

    def test_91(self):
        input = ["INSERT x string", "ASSIGN x _"]
        expected = ["Invalid: ASSIGN x _"]
        self.assertTrue(TestUtils.check(input, expected, 10091))

    def test_92(self):
        input = ["INSERT x number", "ASSIGN x _"]
        expected = ["Invalid: ASSIGN x _"]
        self.assertTrue(TestUtils.check(input, expected, 10092))

    def test_93(self):
        input = ["INSERT x string", "ASSIGN x _b"]
        expected = ["Invalid: ASSIGN x _b"]
        self.assertTrue(TestUtils.check(input, expected, 10093))

    def test_94(self):
        input = ["INSERT x number", "ASSIGN x _b"]
        expected = ["Invalid: ASSIGN x _b"]
        self.assertTrue(TestUtils.check(input, expected, 10094))

    def test_95(self):
        input = ["INSERT x string", "ASSIGN x 3e"]
        expected = ["Invalid: ASSIGN x 3e"]
        self.assertTrue(TestUtils.check(input, expected, 10095))

    def test_96(self):
        input = ["INSERT x number", "ASSIGN x 3e"]
        expected = ["Invalid: ASSIGN x 3e"]
        self.assertTrue(TestUtils.check(input, expected, 10096))

    def test_97(self):
        input = ["INSERT x number", "ASSIGN x bc@ed"]
        expected = ["Invalid: ASSIGN x bc@ed"]
        self.assertTrue(TestUtils.check(input, expected, 10097))

    def test_98(self):
        input = ["INSERT x string", "ASSIGN x bc@ed"]
        expected = ["Invalid: ASSIGN x bc@ed"]
        self.assertTrue(TestUtils.check(input, expected, 10098))

    def test_99(self):
        input = ["INSERT x number", "ASSIGN x bc`ed"]
        expected = ["Invalid: ASSIGN x bc`ed"]
        self.assertTrue(TestUtils.check(input, expected, 10099))

    def test_100(self):
        input = ["INSERT x string", "ASSIGN x bc`ed"]
        expected = ["Invalid: ASSIGN x bc`ed"]
        self.assertTrue(TestUtils.check(input, expected, 10100))

    def test_101(self):
        input = ["INSERT x number", "ASSIGN x bc~ed"]
        expected = ["Invalid: ASSIGN x bc~ed"]
        self.assertTrue(TestUtils.check(input, expected, 10101))

    def test_102(self):
        input = ["INSERT x string", "ASSIGN x bc~ed"]
        expected = ["Invalid: ASSIGN x bc~ed"]
        self.assertTrue(TestUtils.check(input, expected, 10102))

    def test_103(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x y"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10103))

    def test_104(self):
        input = ["INSERT x number", "INSERT y number", "ASSIGN x y"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10104))

    def test_105(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x number"]
        expected = ["Undeclared: ASSIGN x number"]
        self.assertTrue(TestUtils.check(input, expected, 10105))

    def test_106(self):
        input = ["INSERT x number", "INSERT y number", "ASSIGN x string"]
        expected = ["Undeclared: ASSIGN x string"]
        self.assertTrue(TestUtils.check(input, expected, 10106))

    def test_107(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN y number"]
        expected = ["Undeclared: ASSIGN y number"]
        self.assertTrue(TestUtils.check(input, expected, 10107))

    def test_108(self):
        input = ["INSERT x number", "INSERT y number", "ASSIGN y string"]
        expected = ["Undeclared: ASSIGN y string"]
        self.assertTrue(TestUtils.check(input, expected, 10108))

    def test_109(self):
        input = ["INSERT x string", "INSERT y number", "ASSIGN x y"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10109))

    def test_110(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x y"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10110))

    def test_111(self):
        input = ["INSERT x string", "INSERT y number", "ASSIGN y x"]
        expected = ["TypeMismatch: ASSIGN y x"]
        self.assertTrue(TestUtils.check(input, expected, 10111))

    def test_112(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN y x"]
        expected = ["TypeMismatch: ASSIGN y x"]
        self.assertTrue(TestUtils.check(input, expected, 10112))

    def test_113(self):
        input = ["INSERT number number", "INSERT string string", "ASSIGN number string"]
        expected = ["TypeMismatch: ASSIGN number string"]
        self.assertTrue(TestUtils.check(input, expected, 10113))

    def test_114(self):
        input = ["INSERT number number", "INSERT string string", "ASSIGN string number"]
        expected = ["TypeMismatch: ASSIGN string number"]
        self.assertTrue(TestUtils.check(input, expected, 10114))

    def test_115(self):
        input = ["INSERT string string", "INSERT number number", "ASSIGN number string"]
        expected = ["TypeMismatch: ASSIGN number string"]
        self.assertTrue(TestUtils.check(input, expected, 10115))

    def test_116(self):
        input = ["INSERT string string", "INSERT number number", "ASSIGN string number"]
        expected = ["TypeMismatch: ASSIGN string number"]
        self.assertTrue(TestUtils.check(input, expected, 10116))

    def test_117(self):
        input = ["INSERT jennie string", "ASSIGN jennie ''"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10117))

    def test_118(self):
        input = ["ASSIGN a 1"]
        expected = ["Undeclared: ASSIGN a 1"]
        self.assertTrue(TestUtils.check(input, expected, 10118))

    def test_119(self):
        input = ["ASSIGN a 'string'"]
        expected = ["Undeclared: ASSIGN a 'string'"]
        self.assertTrue(TestUtils.check(input, expected, 10119))

    def test_120(self):
        input = ["ASSIGN b2 1"]
        expected = ["Undeclared: ASSIGN b2 1"]
        self.assertTrue(TestUtils.check(input, expected, 10120))

    def test_121(self):
        input = ["ASSIGN b2 'string'"]
        expected = ["Undeclared: ASSIGN b2 'string'"]
        self.assertTrue(TestUtils.check(input, expected, 10121))

    def test_122(self):
        input = ["ASSIGN bE2 1"]
        expected = ["Undeclared: ASSIGN bE2 1"]
        self.assertTrue(TestUtils.check(input, expected, 10122))

    def test_123(self):
        input = ["ASSIGN bE2 'string'"]
        expected = ["Undeclared: ASSIGN bE2 'string'"]
        self.assertTrue(TestUtils.check(input, expected, 10123))

    def test_124(self):
        input = ["ASSIGN bE_2 1"]
        expected = ["Undeclared: ASSIGN bE_2 1"]
        self.assertTrue(TestUtils.check(input, expected, 10124))

    def test_125(self):
        input = ["ASSIGN bE_2 'string'"]
        expected = ["Undeclared: ASSIGN bE_2 'string'"]
        self.assertTrue(TestUtils.check(input, expected, 10125))

    def test_126(self):
        input = ["ASSIGN b_ 1"]
        expected = ["Undeclared: ASSIGN b_ 1"]
        self.assertTrue(TestUtils.check(input, expected, 10126))

    def test_127(self):
        input = ["ASSIGN b_ 'string'"]
        expected = ["Undeclared: ASSIGN b_ 'string'"]
        self.assertTrue(TestUtils.check(input, expected, 10127))

    def test_128(self):
        input = ["ASSIGN b2_ 1"]
        expected = ["Undeclared: ASSIGN b2_ 1"]
        self.assertTrue(TestUtils.check(input, expected, 10128))

    def test_129(self):
        input = ["ASSIGN b2_ 'string'"]
        expected = ["Undeclared: ASSIGN b2_ 'string'"]
        self.assertTrue(TestUtils.check(input, expected, 10129))

    def test_130(self):
        input = ["ASSIGN string 1"]
        expected = ["Undeclared: ASSIGN string 1"]
        self.assertTrue(TestUtils.check(input, expected, 10130))

    def test_131(self):
        input = ["ASSIGN string 'number'"]
        expected = ["Undeclared: ASSIGN string 'number'"]
        self.assertTrue(TestUtils.check(input, expected, 10131))

    def test_132(self):
        input = ["ASSIGN number 1"]
        expected = ["Undeclared: ASSIGN number 1"]
        self.assertTrue(TestUtils.check(input, expected, 10132))

    def test_133(self):
        input = ["ASSIGN number 'number'"]
        expected = ["Undeclared: ASSIGN number 'number'"]
        self.assertTrue(TestUtils.check(input, expected, 10133))

    def test_134(self):
        input = ["INSERT x number", "ASSIGN x a"]
        expected = ["Undeclared: ASSIGN x a"]
        self.assertTrue(TestUtils.check(input, expected, 10134))

    def test_135(self):
        input = ["INSERT x string", "ASSIGN x a"]
        expected = ["Undeclared: ASSIGN x a"]
        self.assertTrue(TestUtils.check(input, expected, 10135))

    def test136(self):
        input = ["INSERT x number", "ASSIGN x b2"]
        expected = ["Undeclared: ASSIGN x b2"]
        self.assertTrue(TestUtils.check(input, expected, 10136))

    def test_137(self):
        input = ["INSERT x string", "ASSIGN x b2"]
        expected = ["Undeclared: ASSIGN x b2"]
        self.assertTrue(TestUtils.check(input, expected, 10137))

    def test_138(self):
        input = ["INSERT x number", "ASSIGN x bE2"]
        expected = ["Undeclared: ASSIGN x bE2"]
        self.assertTrue(TestUtils.check(input, expected, 10138))

    def test_139(self):
        input = ["INSERT x string", "ASSIGN x bE2"]
        expected = ["Undeclared: ASSIGN x bE2"]
        self.assertTrue(TestUtils.check(input, expected, 10139))

    def test_140(self):
        input = ["INSERT x number", "ASSIGN x bE_2"]
        expected = ["Undeclared: ASSIGN x bE_2"]
        self.assertTrue(TestUtils.check(input, expected, 10140))

    def test_141(self):
        input = ["INSERT x string", "ASSIGN x bE_2"]
        expected = ["Undeclared: ASSIGN x bE_2"]
        self.assertTrue(TestUtils.check(input, expected, 10141))

    def test_142(self):
        input = ["INSERT x number", "ASSIGN x b_"]
        expected = ["Undeclared: ASSIGN x b_"]
        self.assertTrue(TestUtils.check(input, expected, 10142))

    def test_143(self):
        input = ["INSERT x string", "ASSIGN x b_"]
        expected = ["Undeclared: ASSIGN x b_"]
        self.assertTrue(TestUtils.check(input, expected, 10143))

    def test_144(self):
        input = ["INSERT x number", "ASSIGN x b2_"]
        expected = ["Undeclared: ASSIGN x b2_"]
        self.assertTrue(TestUtils.check(input, expected, 10144))

    def test_145(self):
        input = ["INSERT x string", "ASSIGN x b2_"]
        expected = ["Undeclared: ASSIGN x b2_"]
        self.assertTrue(TestUtils.check(input, expected, 10145))

    def test_146(self):
        input = ["INSERT x number", "ASSIGN x string"]
        expected = ["Undeclared: ASSIGN x string"]
        self.assertTrue(TestUtils.check(input, expected, 10146))

    def test_147(self):
        input = ["INSERT x string", "ASSIGN x string"]
        expected = ["Undeclared: ASSIGN x string"]
        self.assertTrue(TestUtils.check(input, expected, 10147))

    def test_148(self):
        input = ["INSERT x number", "ASSIGN x number"]
        expected = ["Undeclared: ASSIGN x number"]
        self.assertTrue(TestUtils.check(input, expected, 10148))

    def test_149(self):
        input = ["INSERT x string", "ASSIGN x number"]
        expected = ["Undeclared: ASSIGN x number"]
        self.assertTrue(TestUtils.check(input, expected, 10149))

    def test_150(self):
        input = ["INSERT x string", "ASSIGN x 1"]
        expected = ["TypeMismatch: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10150))

    def test_151(self):
        input = ["INSERT x string", "ASSIGN x 12"]
        expected = ["TypeMismatch: ASSIGN x 12"]
        self.assertTrue(TestUtils.check(input, expected, 10151))

    def test_152(self):
        input = ["INSERT x string", "ASSIGN x 123"]
        expected = ["TypeMismatch: ASSIGN x 123"]
        self.assertTrue(TestUtils.check(input, expected, 10152))

    def test_153(self):
        input = ["INSERT x number", "ASSIGN x 'a'"]
        expected = ["TypeMismatch: ASSIGN x 'a'"]
        self.assertTrue(TestUtils.check(input, expected, 10153))

    def test_154(self):
        input = ["INSERT x number", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10154))

    def test_155(self):
        input = ["INSERT x number", "ASSIGN x '1bc'"]
        expected = ["TypeMismatch: ASSIGN x '1bc'"]
        self.assertTrue(TestUtils.check(input, expected, 10155))

    def test_156(self):
        input = ["INSERT x number", "ASSIGN x '1bC'"]
        expected = ["TypeMismatch: ASSIGN x '1bC'"]
        self.assertTrue(TestUtils.check(input, expected, 10156))

    def test_157(self):
        input = ["INSERT x number", "ASSIGN x 'azAZ09'"]
        expected = ["TypeMismatch: ASSIGN x 'azAZ09'"]
        self.assertTrue(TestUtils.check(input, expected, 10157))

    def test_158(self):
        input = ["INSERT x string", "INSERT y string", " ASSIGN x y"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10158))

    def test_159(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN  x y"]
        expected = ["Invalid: ASSIGN  x y"]
        self.assertTrue(TestUtils.check(input, expected, 10159))

    def test_160(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x  y"]
        expected = ["Invalid: ASSIGN x  y"]
        self.assertTrue(TestUtils.check(input, expected, 10160))

    def test_161(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x y "]
        expected = ["Invalid: ASSIGN x y "]
        self.assertTrue(TestUtils.check(input, expected, 10161))

    def test_162(self):
        input = ["INSERT x string", "INSERT y string", " ASSIGN x 'y'"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10162))

    def test_163(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN  x 'y'"]
        expected = ["Invalid: ASSIGN  x 'y'"]
        self.assertTrue(TestUtils.check(input, expected, 10163))

    def test_164(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x  'y'"]
        expected = ["Invalid: ASSIGN x  'y'"]
        self.assertTrue(TestUtils.check(input, expected, 10164))

    def test_165(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x 'y' "]
        expected = ["Invalid: ASSIGN x 'y' "]
        self.assertTrue(TestUtils.check(input, expected, 10165))

    def test_166(self):
        input = ["INSERT x number", "INSERT y string", " ASSIGN x 1"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10166))

    def test_167(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN  x 1"]
        expected = ["Invalid: ASSIGN  x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10167))

    def test_168(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x  1"]
        expected = ["Invalid: ASSIGN x  1"]
        self.assertTrue(TestUtils.check(input, expected, 10168))

    def test_169(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x 1 "]
        expected = ["Invalid: ASSIGN x 1 "]
        self.assertTrue(TestUtils.check(input, expected, 10169))

    def test_170(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x"]
        expected = ["Invalid: ASSIGN x"]
        self.assertTrue(TestUtils.check(input, expected, 10170))

    def test_171(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x "]
        expected = ["Invalid: ASSIGN x "]
        self.assertTrue(TestUtils.check(input, expected, 10171))

    def test_172(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN  x"]
        expected = ["Invalid: ASSIGN  x"]
        self.assertTrue(TestUtils.check(input, expected, 10172))

    def test_173(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN  "]
        expected = ["Invalid: ASSIGN  "]
        self.assertTrue(TestUtils.check(input, expected, 10173))

    def test_174(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN "]
        expected = ["Invalid: ASSIGN "]
        self.assertTrue(TestUtils.check(input, expected, 10174))

    def test_175(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN"]
        expected = ["Invalid: ASSIGN"]
        self.assertTrue(TestUtils.check(input, expected, 10175))

    """=====================================================BEGIN+END======================================================"""

    def test_176(self):
        input = ["BEGIN", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10176))

    def test_177(self):
        input = ["BEGIN ", "END"]
        expected = ["Invalid: BEGIN "]
        self.assertTrue(TestUtils.check(input, expected, 10177))

    def test_178(self):
        input = [" BEGIN", "END"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10178))

    def test_179(self):
        input = ["BEGIN  ", "END"]
        expected = ["Invalid: BEGIN  "]
        self.assertTrue(TestUtils.check(input, expected, 10179))

    def test_180(self):
        input = ["INSERT x number", "BEGIN x", "END"]
        expected = ["Invalid: BEGIN x"]
        self.assertTrue(TestUtils.check(input, expected, 10180))

    def test_181(self):
        input = ["BEGIN", "END "]
        expected = ["Invalid: END "]
        self.assertTrue(TestUtils.check(input, expected, 10181))

    def test_182(self):
        input = ["BEGIN", " END"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10182))

    def test_183(self):
        input = ["BEGIN", "END  "]
        expected = ["Invalid: END  "]
        self.assertTrue(TestUtils.check(input, expected, 10183))

    def test_184(self):
        input = ["INSERT x number", "BEGIN", "END x"]
        expected = ["Invalid: END x"]
        self.assertTrue(TestUtils.check(input, expected, 10184))

    def test_185(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10185))

    def test_186(self):
        input = ["INSERT x number", "BEGIN", "INSERT x string", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10186))

    def test_187(self):
        input = ["INSERT x string", "BEGIN", "INSERT x string", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10187))

    def test_188(self):
        input = ["INSERT x string", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10188))

    def test_189(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "ASSIGN x 1", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10189))

    def test_190(self):
        input = ["INSERT x string", "BEGIN", "INSERT x number", "ASSIGN x 1", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10190))

    def test_191(self):
        input = ["INSERT x number", "BEGIN", "INSERT x string", "ASSIGN x 1", "END"]
        expected = ["TypeMismatch: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10191))

    def test_192(self):
        input = ["INSERT x string", "BEGIN", "INSERT x string", "ASSIGN x 1", "END"]
        expected = ["TypeMismatch: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10192))

    def test_193(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "ASSIGN x '1'", "END"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10193))

    def test_194(self):
        input = ["INSERT x string", "BEGIN", "INSERT x number", "ASSIGN x '1'", "END"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10194))

    def test_195(self):
        input = ["INSERT x number", "BEGIN", "INSERT x string", "ASSIGN x '1'", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10195))

    def test_196(self):
        input = ["INSERT x string", "BEGIN", "INSERT x string", "ASSIGN x '1'", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10196))

    def test_197(self):
        input = ["INSERT x string", "INSERT y number", "BEGIN", "INSERT x number", "ASSIGN x y", "END"]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10197))

    def test_198(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x number", "ASSIGN x y", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10198))

    def test_199(self):
        input = ["INSERT x number", "INSERT y string", "BEGIN", "INSERT y number", "ASSIGN x y", "END"]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10199))

    def test_200(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT y number", "ASSIGN x y", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10200))

    def test_201(self):
        input = ["BEGIN", "BEGIN", "END", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10201))

    def test_202(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END", "END", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10202))

    def test_203(self):
        input = ["BEGIN", "BEGIN", "END", "END", "BEGIN", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10203))

    def test_204(self):
        input = ["BEGIN", "BEGIN", "END", "END", "BEGIN", "BEGIN", "END", "END",]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10204))

    def test_205(self):
        input = ["BEGIN", "BEGIN", "END", "BEGIN", "END", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10205))

    def test_206(self):
        input = ["BEGIN", "BEGIN", "END", "BEGIN", "END", "END", "BEGIN", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10206))

    def test_207(self):
        input = ["BEGIN", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10207))

    def test_208(self):
        input = ["BEGIN", "BEGIN", "END", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10208))

    def test_209(self):
        input = ["BEGIN", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10209))

    def test_210(self):
        input = ["BEGIN", "BEGIN", "END", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10210))

    def test_211(self):
        input = ["END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10211))

    def test_212(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "END", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10212))

    def test_213(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "END"]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10213))

    def test_214(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "END", "END", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10214))

    def test_215(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END",]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10215))

    def test_216(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10216))

    def test_217(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END", "END", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10217))

    def test_218(self):
        input = ["BEGIN", "INSERT x number", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10218))

    def test_219(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10219))

    def test_220(self):
        input = ["BEGIN", "INSERT x number", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10220))

    def test_221(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "END", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10221))

    def test_222(self):
        input = ["INSERT x number", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10222))

    def test_223(self):
        input = ["BEGIN"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10223))

    def test_224(self):
        input = ["BEGIN", "BEGIN"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10224))

    def test_225(self):
        input = ["BEGIN", "BEGIN", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10225))

    def test_226(self):
        input = ["BEGIN", "BEGIN", "BEGIN"]
        expected = ["UnclosedBlock: 3"]
        self.assertTrue(TestUtils.check(input, expected, 10226))

    def test_227(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10227))

    def test_228(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10228))

    def test_229(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END", "BEGIN", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10229))

    def test_230(self):
        input = ["BEGIN", "BEGIN", "END", "END", "BEGIN", "BEGIN", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10230))

    def test_231(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10231))

    def test_232(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10232))

    def test_233(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10233))

    def test_234(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", ]
        expected = ["UnclosedBlock: 3"]
        self.assertTrue(TestUtils.check(input, expected, 10234))

    def test_235(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10235))

    def test_236(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10236))

    def test_237(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10237))

    def test_238(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "END", "END", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10238))

    def test_239(self):
        input = ["INSERT x number", "BEGIN", "BEGIN", "INSERT x number", "END", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10239))

    def test_240(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10240))

    def test_241(self):
        input = ["INSERT x number", "BEGIN", "BEGIN", "INSERT x number", "END", "INSERT x number", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10241))

    def test_242(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "INSERT x number", "END"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 10242))

    def test_243(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "INSERT x number"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 10243))

    def test_244(self):
        input = ["BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10244))

    def test_245(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10245))

    def test_246(self):
        input = ["INSERT x number", "INSERT y string", "BEGIN", "INSERT x number", "INSERT y string", "END", "BEGIN", "INSERT x number", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10246))

    def test_247(self):
        input = ["BEGIN", "INSERT x number", "END", "INSERT x number", "BEGIN", "INSERT x number", "END", "INSERT x number"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 10247))

    def test_248(self):
        input = ["BEGIN", "BEGIN", "ASSIGN x y", "END", "END"]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10248))

    def test_249(self):
        input = ["INSERT x number", "BEGIN", "INSERT y number", "BEGIN", "ASSIGN x y", "END", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10249))

    def test_250(self):
        input = ["INSERT x string", "BEGIN", "INSERT y number", "BEGIN", "ASSIGN x y", "END", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10250))

    def test_251(self):
        input = ["INSERT x string", "BEGIN", "INSERT y number", "BEGIN", "INSERT z number", "ASSIGN x y", "END", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10251))

    def test_252(self):
        input = ["INSERT x number", "BEGIN", "INSERT y string", "BEGIN", "INSERT z number", "ASSIGN x y", "END", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10252))

    def test_253(self):
        input = ["INSERT x number", "BEGIN", "INSERT y number", "BEGIN", "INSERT z string", "ASSIGN x y", "END", "END"]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10253))

    def test_254(self):
        input = ["INSERT x number", "BEGIN", "INSERT x string", "INSERT y number", "BEGIN", "INSERT y string", "INSERT z number", "ASSIGN x y", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10254))

    def test_255(self):
        input = ["BEGIN", "INSERT x string", "INSERT y number", "BEGIN", "END", "END", "ASSIGN x y"]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10255))

    def test_256(self):
        input = ["BEGIN", "INSERT x number", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "ASSIGN y x", "END"]
        expected = ["Undeclared: ASSIGN y x"]
        self.assertTrue(TestUtils.check(input, expected, 10256))

    def test_257(self):
        input = ["INSERT x number", "INSERT y number", "BEGIN", "INSERT x number", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "ASSIGN y x", "END"]
        expected = ["success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10257))

    def test_258(self):
        input = ["BEGIN", "INSERT x number", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "INSERT x number", "INSERT y number", "ASSIGN y x", "END", "ASSIGN x y"]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10258))

    def test_259(self):
        input = ["INSERT x number", "INSERT y number", "BEGIN", "INSERT x number", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "INSERT x number", "INSERT y number", "ASSIGN y x", "END", "ASSIGN x y"]
        expected = ["success", "success", "success", "success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10259))

    def test_260(self):
        input = ["INSERT x number", "INSERT y number", "BEGIN", "INSERT x string", "INSERT y string", "ASSIGN x y", "END", "BEGIN", "INSERT x string", "INSERT y string", "ASSIGN y x", "END", "ASSIGN x y"]
        expected = ["success", "success", "success", "success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10260))

    def test_261(self):
        input = ["INSERT x number", "INSERT y number", "BEGIN", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "INSERT x number", "ASSIGN y x", "END", "ASSIGN x y"]
        expected = ["success", "success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10261))

    def test_262(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "ASSIGN x y", "END", "INSERT x number", "INSERT y number", "BEGIN", "INSERT x string", "INSERT y string", "ASSIGN y x", "END", "ASSIGN x y"]
        expected = ["success", "success", "success", "success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10262))

    def test_263(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10263))

    def test_264(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10264))

    def test_265(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10265))

    def test_266(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10266))

    def test_267(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10267))

    def test_268(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10268))

    def test_269(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10269))

    def test_270(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "END", "END", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10270))

    def test_271(self):
        input = ["BEGIN", "ASSIGN x 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["Undeclared: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10271))

    def test_272(self):
        input = ["BEGIN", "ASSIGN y 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["Undeclared: ASSIGN y 1"]
        self.assertTrue(TestUtils.check(input, expected, 10272))

    def test_273(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "ASSIGN x 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["TypeMismatch: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10273))

    def test_274(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "ASSIGN y 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["TypeMismatch: ASSIGN y 1"]
        self.assertTrue(TestUtils.check(input, expected, 10274))
    
    def test_275(self):
        input = ["BEGIN", "INSERT y number", "ASSIGN x 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["Undeclared: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10275))

    def test_276(self):
        input = ["BEGIN", "INSERT x number", "ASSIGN y 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["Undeclared: ASSIGN y 1"]
        self.assertTrue(TestUtils.check(input, expected, 10276))

    """=====================================================LOOKUP======================================================"""

    def test_277(self):
        input = ["LOOKUP B"]
        expected = ["Invalid: LOOKUP B"]
        self.assertTrue(TestUtils.check(input, expected, 10277))

    def test_278(self):
        input = ["LOOKUP Ba"]
        expected = ["Invalid: LOOKUP Ba"]
        self.assertTrue(TestUtils.check(input, expected, 10278))

    def test_279(self):
        input = ["LOOKUP B2"]
        expected = ["Invalid: LOOKUP B2"]
        self.assertTrue(TestUtils.check(input, expected, 10279))

    def test_280(self):
        input = ["LOOKUP _"]
        expected = ["Invalid: LOOKUP _"]
        self.assertTrue(TestUtils.check(input, expected, 10280))

    def test_281(self):
        input = ["LOOKUP _b"]
        expected = ["Invalid: LOOKUP _b"]
        self.assertTrue(TestUtils.check(input, expected, 10281))

    def test_282(self):
        input = ["LOOKUP 3e"]
        expected = ["Invalid: LOOKUP 3e"]
        self.assertTrue(TestUtils.check(input, expected, 10282))

    def test_283(self):
        input = ["LOOKUP bc@ed"]
        expected = ["Invalid: LOOKUP bc@ed"]
        self.assertTrue(TestUtils.check(input, expected, 10283))

    def test_284(self):
        input = ["LOOKUP bc`ed"]
        expected = ["Invalid: LOOKUP bc`ed"]
        self.assertTrue(TestUtils.check(input, expected, 10284))

    def test_285(self):
        input = ["LOOKUP bc~ed"]
        expected = ["Invalid: LOOKUP bc~ed"]
        self.assertTrue(TestUtils.check(input, expected, 10285))

    def test_286(self):
        input = ["LOOKUP a"]
        expected = ["Undeclared: LOOKUP a"]
        self.assertTrue(TestUtils.check(input, expected, 10286))

    def test_287(self):
        input = ["LOOKUP b2"]
        expected = ["Undeclared: LOOKUP b2"]
        self.assertTrue(TestUtils.check(input, expected, 10287))

    def test_288(self):
        input = ["LOOKUP bE2"]
        expected = ["Undeclared: LOOKUP bE2"]
        self.assertTrue(TestUtils.check(input, expected, 10288))

    def test_289(self):
        input = ["LOOKUP bE_2"]
        expected = ["Undeclared: LOOKUP bE_2"]
        self.assertTrue(TestUtils.check(input, expected, 10289))

    def test_290(self):
        input = ["LOOKUP b_"]
        expected = ["Undeclared: LOOKUP b_"]
        self.assertTrue(TestUtils.check(input, expected, 10290))

    def test_291(self):
        input = ["LOOKUP b2_"]
        expected = ["Undeclared: LOOKUP b2_"]
        self.assertTrue(TestUtils.check(input, expected, 10291))

    def test_292(self):
        input = ["LOOKUP string"]
        expected = ["Undeclared: LOOKUP string"]
        self.assertTrue(TestUtils.check(input, expected, 10292))

    def test_293(self):
        input = ["LOOKUP number"]
        expected = ["Undeclared: LOOKUP number"]
        self.assertTrue(TestUtils.check(input, expected, 10293))

    def test_294(self):
        input = ["LOOKUP x "]
        expected = ["Invalid: LOOKUP x "]
        self.assertTrue(TestUtils.check(input, expected, 10294))

    def test_295(self):
        input = ["LOOKUP "]
        expected = ["Invalid: LOOKUP "]
        self.assertTrue(TestUtils.check(input, expected, 10295))

    def test_296(self):
        input = ["LOOKUP"]
        expected = ["Invalid: LOOKUP"]
        self.assertTrue(TestUtils.check(input, expected, 10296))

    def test_297(self):
        input = [" LOOKUP x"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10297))

    def test_298(self):
        input = ["INSERT x number", "LOOKUP x x"]
        expected = ["Invalid: LOOKUP x x"]
        self.assertTrue(TestUtils.check(input, expected, 10298))

    def test_299(self):
        input = ["LOOKUP  x"]
        expected = ["Invalid: LOOKUP  x"]
        self.assertTrue(TestUtils.check(input, expected, 10299))

    def test_300(self):
        input = ["INSERT x number", "LOOKUP x"]
        expected = ["success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10300))

    def test_301(self):
        input = ["INSERT x number", "INSERT y number", "LOOKUP x"]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10301))

    def test_302(self):
        input = ["INSERT x string", "INSERT y number", "LOOKUP x"]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10302))

    def test_303(self):
        input = ["INSERT y number", "LOOKUP x"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10303))

    def test_304(self):
        input = ["INSERT x number", "BEGIN", "LOOKUP x", "END"]
        expected = ["success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10304))

    def test_305(self):
        input = ["BEGIN", "INSERT x number", "LOOKUP x", "END"]
        expected = ["success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10305))

    def test_306(self):
        input = ["BEGIN", "INSERT x number", "LOOKUP x", "END"]
        expected = ["success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10306))

    def test_307(self):
        input = ["BEGIN", "INSERT x number", "BEGIN",  "LOOKUP x", "END", "END"]
        expected = ["success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10307))

    def test_308(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "2"]
        self.assertTrue(TestUtils.check(input, expected, 10308))

    def test_309(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10309))

    def test_310(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10310))

    def test_311(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "LOOKUP x", "END"]
        expected = ["success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10311))

    def test_312(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "LOOKUP x"]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10312))

    def test_313(self):
        input = ["BEGIN", "BEGIN", "INSERT x number", "END", "LOOKUP x", "END"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10313))

    def test_314(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "LOOKUP x"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10314))

    def test_315(self):
        input = ["INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "LOOKUP x", "END"]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10315))

    def test_316(self):
        input = ["BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "LOOKUP x", "END"]
        expected = ["success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10316))

    def test_317(self):
        input = ["BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "LOOKUP x", "END"]
        expected = ["success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10317))

    def test_318(self):
        input = ["BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN",  "LOOKUP x", "END", "END"]
        expected = ["success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10318))

    def test_319(self):
        input = ["BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "2"]
        self.assertTrue(TestUtils.check(input, expected, 10319))

    def test_320(self):
        input = ["INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10320))

    def test_321(self):
        input = ["INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10321))

    def test_322(self):
        input = ["INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "END", "LOOKUP x", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10322))

    def test_323(self):
        input = ["INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "END", "END", "LOOKUP x"]
        expected = ["success", "success", "success", "success", "success", "success", "success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10323))

    def test_324(self):
        input = ["BEGIN", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "END", "LOOKUP x", "END"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10324))

    def test_325(self):
        input = ["BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "END", "END", "LOOKUP x"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10325))

    def test_326(self):
        input = ["BEGIN", "LOOKUP x", "INSERT x number",  "END"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10326))

    def test_327(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "INSERT x number", "END", "END"]
        expected = ["success", "1", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10327))

    def test_328(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "INSERT x number", "END", "END"]
        expected = ["success", "success", "1", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10328))

    def test_329(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "LOOKUP x", "END"]
        expected = ["success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10329))

    def test_330(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "LOOKUP x", "END"]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10330))

    def test_331(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END", "LOOKUP x"]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10331))

    def test_332(self):
        input = ["BEGIN", "INSERT x number", "END", "INSERT x number", "BEGIN", "INSERT x number", "END", "LOOKUP x"]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10332))

    """=====================================================PRINT======================================================"""

    def test_333(self):
        input = ["PRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10333))

    def test_334(self):
        input = ["PRINT "]
        expected = ["Invalid: PRINT "]
        self.assertTrue(TestUtils.check(input, expected, 10334))

    def test_335(self):
        input = [" PRINT"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10335))

    def test_336(self):
        input = ["PRINT  "]
        expected = ["Invalid: PRINT  "]
        self.assertTrue(TestUtils.check(input, expected, 10336))

    def test_337(self):
        input = ["PRINT number"]
        expected = ["Invalid: PRINT number"]
        self.assertTrue(TestUtils.check(input, expected, 10337))

    def test_338(self):
        input = ["INSERT x number", "PRINT x"]
        expected = ["Invalid: PRINT x"]
        self.assertTrue(TestUtils.check(input, expected, 10338))

    def test_339(self):
        input = ["INSERT x number", "INSERT y number", "PRINT"]
        expected = ["success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10339))

    def test_340(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", ""]
        self.assertTrue(TestUtils.check(input, expected, 10340))

    def test_341(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "PRINT", "END"]
        expected = ["success", "success", "x//1 y//1"]
        self.assertTrue(TestUtils.check(input, expected, 10341))

    def test_342(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "PRINT", "END"]
        expected = ["success", "success", "success", "success", "x//1 y//1"]
        self.assertTrue(TestUtils.check(input, expected, 10342))

    def test_343(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "success","x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10343))

    def test_344(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "PRINT", "END"]
        expected = ["success", "success", "success", "y//0 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10344))

    def test_345(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10345))

    def test_346(self):
        input = ["PRINT", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10346))

    def test_347(self):
        input = ["PRINT", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10347))

    def test_348(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "PRINT", "END", "INSERT x string", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "x//2 y//2", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10348))

    def test_349(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "INSERT y string", "PRINT", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "x//1 y//1"]
        self.assertTrue(TestUtils.check(input, expected, 10349))

    def test_350(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10350))

    def test_351(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10351))

    def test_352(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "x//0 y//0", "success", "success", ]
        self.assertTrue(TestUtils.check(input, expected, 10352))

    def test_353(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10353))

    def test_354(self):
        input = ["INSERT x string", "INSERT y string", "INSERT z string", "PRINT"]
        expected = ["success", "success", "success", "x//0 y//0 z//0"]
        self.assertTrue(TestUtils.check(input, expected, 10354))

    def test_355(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT z string", "PRINT", "END"]
        expected = ["success", "success", "success", "x//0 y//0 z//1"]
        self.assertTrue(TestUtils.check(input, expected, 10355))

    def test_356(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT z string", "PRINT", "END"]
        expected = ["success", "success", "success", "success", "x//0 y//0 z//1"]
        self.assertTrue(TestUtils.check(input, expected, 10356))

    def test_357(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT z string", "PRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "y//0 x//1 z//2"]
        self.assertTrue(TestUtils.check(input, expected, 10357))

    def test_358(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "PRINT", "INSERT z string", "END", "END"]
        expected = ["success", "success", "success", "success", "z//0 y//0 x//1", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10358))

    def test_359(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT y string", "INSERT z string", "PRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "x//1 y//2 z//2"]
        self.assertTrue(TestUtils.check(input, expected, 10359))

    """=====================================================RPRINT======================================================"""

    def test_360(self):
        input = ["RPRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10360))

    def test_361(self):
        input = ["RPRINT "]
        expected = ["Invalid: RPRINT "]
        self.assertTrue(TestUtils.check(input, expected, 10361))

    def test_362(self):
        input = [" RPRINT"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10362))

    def test_363(self):
        input = ["RPRINT  "]
        expected = ["Invalid: RPRINT  "]
        self.assertTrue(TestUtils.check(input, expected, 10363))

    def test_364(self):
        input = ["RPRINT number"]
        expected = ["Invalid: RPRINT number"]
        self.assertTrue(TestUtils.check(input, expected, 10364))

    def test_365(self):
        input = ["INSERT x number", "RPRINT x"]
        expected = ["Invalid: RPRINT x"]
        self.assertTrue(TestUtils.check(input, expected, 10365))

    def test_366(self):
        input = ["INSERT x number", "INSERT y number", "RPRINT"]
        expected = ["success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10366))

    def test_367(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", ""]
        self.assertTrue(TestUtils.check(input, expected, 10367))

    def test_368(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "RPRINT", "END"]
        expected = ["success", "success", "y//1 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10368))

    def test_369(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "RPRINT", "END"]
        expected = ["success", "success", "success", "success", "y//1 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10369))

    def test_370(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success","y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10370))

    def test_371(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "RPRINT", "END"]
        expected = ["success", "success", "success", "x//1 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10371))

    def test_372(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10372))

    def test_373(self):
        input = ["RPRINT", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10373))

    def test_374(self):
        input = ["RPRINT", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10374))

    def test_375(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "RPRINT", "END", "INSERT x string", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "y//2 x//2", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10375))

    def test_376(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "INSERT y string", "RPRINT", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "y//1 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10376))

    def test_377(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10377))

    def test_378(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10378))

    def test_379(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "y//0 x//0", "success", "success", ]
        self.assertTrue(TestUtils.check(input, expected, 10379))

    def test_380(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10380))

    def test_381(self):
        input = ["INSERT x string", "INSERT y string", "INSERT z string", "RPRINT"]
        expected = ["success", "success", "success", "z//0 y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10381))

    def test_382(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT z string", "RPRINT", "END"]
        expected = ["success", "success", "success", "z//1 y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10382))

    def test_383(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT z string", "RPRINT", "END"]
        expected = ["success", "success", "success", "success", "z//1 y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10383))

    def test_384(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT z string", "RPRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "z//2 x//1 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10384))

    def test_385(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "RPRINT", "INSERT z string", "END", "END"]
        expected = ["success", "success", "success", "success", "x//1 y//0 z//0", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10385))

    def test_386(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT y string", "INSERT z string", "RPRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "z//2 y//2 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10386))

    """=====================================================OTHER======================================================"""

    def test_387(self):
        input = [""]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10387))

    def test_388(self):
        input = [" "]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10388))

    def test_389(self):
        input = ["  "]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10389))

    def test_390(self):
        input = []
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10390))

    def test_391(self):
        input = ["INSERT x number", ""]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10391))

    def test_392(self):
        input = ["INSERT x number", "", "INSERT x number"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10392))

    def test_393(self):
        input = ["INSErT x number"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10393))

    def test_394(self):
        input = ["x INSERT number"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10394))

    def test_395(self):
        input = ["INSERT x", "number INSERT y number"]
        expected = ["Invalid: INSERT x"]
        self.assertTrue(TestUtils.check(input, expected, 10395))

    def test_396(self):
        input = ["INSERT x number INSERT y number"]
        expected = ["Invalid: INSERT x number INSERT y number"]
        self.assertTrue(TestUtils.check(input, expected, 10396))

    def test_397(self):
        input = ["INSERT x number", " "]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10397))

    def test_398(self):
        input = ["INSERT x number", "  "]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10398))

    def test_399(self):
        input = ["INSERT x number", "   "]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10399))