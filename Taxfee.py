#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 党费，个税,五险一金缴纳金额计算器

import sys

class All_taxes_fee():
    '''各种费用缴纳类'''
    def __init__(self,salary,partymember):
        self.partymember = self.ispartymember(partymember)
        self.salary  = salary 
        self.tax_gap = [0,0,90,990,3590,6090,12090,20840]
        self.incomes = [5000,8000,17000,30000,40000,60000,85000]
        self.income_party = [3000,5000,10000]
        self.partyfee_gap = [0,15,35,110]
        self.tax_fee = 0
        self.income_level = ['贫困级','温饱级','伪小康级','真小康级','中产级','富人级','富翁级','富豪级']
        self.insur   = {
                                "Pension":[0.08,0.2],
                                "Medical":[0.02,0.1],
                                 "Unemployment":[0.002,0.01],
                                "Injury":[0,0.003],
                                "Birth":[0,0.008],
                                "HousingFund":[0.12,0.12]
                       }

    def ispartymember(self,partymember):
        if partymember == "y" or partymember == "Y":
            return True 
        else:
            return False

    def pension(self):
        '''养老金缴纳'''
        employee_part = round(self.insur['Pension'][0]*self.salary,2)
        company_part  = round(self.insur['Pension'][1]*self.salary,2)
        return [employee_part, company_part]

    def medical(self):
        '''医疗保险缴纳'''
        employee_part = round(self.insur['Medical'][0]*self.salary,2)
        company_part  = round(self.insur['Medical'][1]*self.salary,2)
        return [employee_part, company_part]

    def unemployment(self):
        '''失业保险缴纳'''
        employee_part = round(self.insur['Unemployment'][0]*self.salary,2)
        company_part  = round(self.insur['Unemployment'][1]*self.salary,2)
        return [employee_part, company_part]

    def injury(self):
        '''工伤保险缴纳'''
        employee_part = round(self.insur['Injury'][0]*self.salary,2)
        company_part  = round(self.insur['Injury'][1]*self.salary,2)
        return [employee_part, company_part]

    def birth(self):
        '''生育保险缴纳'''
        employee_part = round(self.insur['Birth'][0]*self.salary,2)
        company_part  = round(self.insur['Birth'][1]*self.salary,2)
        return [employee_part, company_part]

    def housingfund(self):
        '''住房公积金缴纳'''
        employee_part = round(self.insur['HousingFund'][0]*self.salary,2)
        company_part  = round(self.insur['HousingFund'][1]*self.salary,2)
        return [employee_part, company_part]

    def taxcalc(self):
        '''个人所得税计算'''
        if self.incomes[0]>= self.salary >= 0:
            order = 1
            tax = self.tax_gap[0]
        elif self.incomes[1] >= self.salary >self.incomes[0]:
            order = 2
            tax = (self.salary - 5000)*0.03 + self.tax_gap[1]
        elif self.incomes[2]>= self.salary >self.incomes[1]:
            order = 3
            tax = (self.salary - 8000)*0.10 + self.tax_gap[2]
        elif self.incomes[3]>= self.salary >self.incomes[2]:
            order = 4
            tax = (self.salary - 17000)*0.20 + self.tax_gap[3]
        elif self.incomes[4]>= self.salary >self.incomes[3]:
            order = 5
            tax = (self.salary - 30000)*0.25 + self.tax_gap[4]
        elif self.incomes[5]>= self.salary >self.incomes[4]:
            order = 6
            tax = (self.salary - 40000)*0.30 + self.tax_gap[5]
        elif self.incomes[6]>= self.salary >self.incomes[5]:
            order = 7
            tax = (self.salary - 60000)*0.35 + self.tax_gap[6]
        elif self.salary >self.incomes[6]:
            order = 8
            tax = (self.salary - 85000)*0.45 + self.tax_gap[7]
        else:
            return [None,0]

        #print("你的收入等级:%d级, 应缴税款:%.2f元"%(order,round(tax,2))) 
        return [order,round(tax,2)]

    def partyfeecalc(self):
        '''党费计算'''
        if not self.partymember:
            return [None,0]
        new_base = self.salary - self.tax_fee

        if self.income_party[0]>= new_base >= 0:
            order = 1
            partyfee = self.salary*0.005 + self.partyfee_gap[0]
        elif self.income_party[1] >= new_base >self.income_party[0]:
            order = 2
            partyfee = (self.salary - 3000)*0.01 + self.partyfee_gap[1]
        elif self.income_party[2] >= new_base >self.income_party[1]:
            order = 3
            partyfee = (self.salary - 5000)*0.015 + self.partyfee_gap[2]
        elif new_base >self.income_party[2]:
            order = 4
            partyfee = (self.salary - 10000)*0.02 + self.partyfee_gap[3]
        else:
            return [None,0]

        self.income_party = [3000,5000,10000]
        #print("你的收入等级:%d级, 应缴党费:%.2f元"%(order,round(partyfee,2))) 
        return [order,round(partyfee,2)]

    def main(self):
        pension = self.pension()
        medical = self.medical()
        unemploy= self.unemployment()
        injury  = self.injury()
        birth   = self.birth()
        housing = self.housingfund()
        tax     = self.taxcalc()

        self.tax_fee  = self.salary - tax[1] 
        partyfee= self.partyfeecalc()

        print(" ")    
        print("以下是您及公司缴纳的各项费用的统计数据（第一项为个人缴纳，第二项为公司缴纳)：")    
        print("-----------------五险一金的缴纳情况---------------------")    
        print("养老保险缴纳比例分别为：%d%%\t%d%%"%(self.insur['Pension'][0]*100,
                self.insur['Pension'][1]*100))    

        print("医疗保险缴纳比例分别为：%d%%\t%d%%"%(self.insur['Medical'][0]*100,
                self.insur['Medical'][1]*100))    

        print("失业保险缴纳比例分别为：%d%%\t%d%%"%(self.insur['Unemployment'][0]*100,
                self.insur['Unemployment'][1]*100))    

        print("工伤保险缴纳比例分别为：%d%%\t%d%%"%(self.insur['Injury'][0]*100,
                self.insur['Injury'][1]*100))    

        print("生育保险缴纳比例分别为：%d%%\t%d%%"%(self.insur['Birth'][0]*100,
                self.insur['Birth'][1]*100))    

        print("住房公积缴纳比例分别为：%d%%\t%d%%"%(self.insur['HousingFund'][0]*100,
                self.insur['HousingFund'][1]*100))    

        print("养老保险缴纳金额分别为：%.2f\t%.2f"%(pension[0],pension[1]))    
        print("医疗保险缴纳金额分别为：%.2f\t%.2f"%(medical[0],medical[1]))    
        print("失业保险缴纳金额分别为：%.2f\t%.2f"%(unemploy[0],unemploy[1]))    
        print("工伤保险缴纳金额分别为：%.2f\t%.2f"%(injury[0],injury[1]))    
        print("生育保险缴纳金额分别为：%.2f\t%.2f"%(birth[0],birth[1]))    
        print("住房公积缴纳金额分别为：%.2f\t%.2f"%(housing[0],housing[1]))    


        print("")
        print("------------------税费及党费的缴纳情况-------------------")    
        print("个人所得税税率及党费缴纳均按照收入分等级(1~8级)")
        print("个税等级区间点[5000,8000,17000,30000,40000,60000,85000]")
        print("党费等级区间点[3000,5000,10000](税后)")
        print("收入等级可分为[贫困级,温饱级,伪小康级,真小康级,中产级,富人级,富翁级,富豪级]")
        print("你的收入等级：%d级，属于：%s"%(tax[0],self.income_level[tax[0]-1]))
        print("个税起征点：5000元，您应缴所得税为：%.2f元"%tax[1])
        if not self.partymember:
            print("党费起征点：1元，您不是共产党员，所以无需缴纳党费")
        else:
            print("党费起征点：1元，您属于共产党员，应缴党费：%.2f元"%partyfee[1])

        allfees_person = pension[0]+medical[0]+unemploy[0]+injury[0]+birth[0]+housing[0]+tax[1]+partyfee[1]
        allfees_company= pension[1]+medical[1]+unemploy[1]+injury[1]+birth[1]+housing[1]

        fivefees = pension[0]+medical[0]+unemploy[0]+injury[0]+birth[0]+housing[0]

        left = self.salary - allfees_person

        ratio_person = (100*allfees_person+0.0)/self.salary
        ratio_company= (100*allfees_company+0.0)/self.salary

        all_tax = allfees_person + allfees_company
        all_cost = self.salary + allfees_company
        all_ratio = (100*all_tax+0.0)/all_cost

        print("")
        print("---------------------合计--------------------------------")    
        print("您的税前月工资：%.2f元，实际缴纳各种费用：%.2f元\n其中五险一金为：%.2f元，纳税：%.2f元，党费：%.2f元\n你实际拿到工资：%.2f元，占税前工资%.2f%%"%(self.salary,allfees_person,fivefees,tax[1],partyfee[1],left,ratio_person))    
        print("公司纳五险一金：%.2f元，占税前工资%.2f%%"%(allfees_company,ratio_company))    
        print("公司总共支出额：%.2f元，双方共缴各种费用：%.2f元，占比为：%.2f%%"%(all_cost,all_tax,all_ratio))    



if __name__ == "__main__":
    salary = round(float(input("请输入您的税前月工资：")),2)
    partymember = str(input("请问你是党员吗(y/n)："))

    taxes_fee = All_taxes_fee(salary,partymember)
    taxes_fee.main()
