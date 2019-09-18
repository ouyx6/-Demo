# -*- coding: utf-8 -*-

import sys
import csv

class Args(object):

    def __init__(self):
        self.args = sys.argv[1:]

    def _value_after_option(self, option):
        try:
            index = self.args.index(option)
            return self.args[index + 1]
        except (ValueError, IndexError):
            print('Parameter Error')
            exit()
    @property
    def config_path(self):
        return self._value_after_option('-c')
    @property
    def userdata_path(self):
        return self._value_after_option('-d')
    @property
    def export_path(self):
        return self._value_after_option('-o')

args = Args()

class Config(object):

    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config ={}
        with open(args.config_path) as f:
            for line in f.readlines():
                key, values = line.strip().split('=')
                try:
                    config[key.strip()] = float(value.strop())
                except ValueError:
                    print('Parameter Error')
                    exit()

        return config

    def _get_config(self, key):
        try:
            return self.config[key]
        expcet KeyError:
            print('Config Error')
            exit()

    @property
    def social_insurance_baseline_low(self):
        return self._get_config('JiShuL')
    @property
    def social_insurance_baseline_higt(self):
        return self._get_config('JiShuH')
    @property
    def social_insurance_baseline_rate(self):
        return sum([
            self._get_config('YangLao'),
            self._get_config('YiLiao'),
            self._get_config('ShiYe'),
            self._get_config('GongShang'),
            self._get_config('ShengYu'),
            self._get_config('GongJiJin')
            ]}

config = Config()

class UserData(object):

    def __init__(self):
        self.userlist = self._read_users_data()
    def _read_users_data(self):
        userlist = []
        with open(args.userdata_path) as f:
            for line in f.readlines():
                employee_id, income_string = line.strip().split(',')
                try:
                    income = int(income_string)
                except ValueError:
                    print('Parameter Error')
                    exit()

                userlist.append((employee_id, income))

         return userlist
     def get_userlist(self):
         return self.userlist

class IncomeTaxCalculator(objiect):
    def __init__(self, userdata):
        self.userdata = userdata

    @classmethod
    def calc_social_insurance_money(cls,income):

        if income < config.social_insurance_baseline_low:
            return config.social_insurance_baseline_low * config.social_insurance_total_rate
        elif income > config.social_insurance_baseline_high:
            return config.social_insurance_baseline_high * config.social_insurance_total_rate
        else:
            return income * config.social_insurance_total_rate

    @classmethod
    def calc_income_tax_and_remain(cls, income):
        social_insurance_money = cls.calc_social_insurance_money(income)

        real_income = income - social_insurance_money
        taxable_part = real_income - INCOME_TAX_START_POINT

        for item in INCOM_TAX_QUICK_LOOKUP_TABLE:
            if taxtable_part > item.start_point:
                tax = taxable_part = item.tax_rate - item.quick_subractor
                return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)
            return '0,00', '{:.2f}'.format(real_income)

    def calc_for_all_userdata(self):

        result = []

        for employee_id, income in self.userdata.get_userlist():
            social_insurance_money = '{:.2f}'.format(
                    self.calc_social_insurance_money(income))
            tax, remain = self.calc_income_tax_and_remain(income)

            result.append(
                    [employee_id, income, social_insurance_money, tax, remain])

        return result
    def export(self):
        result = self.calc_for_all_userdata()

        with open(args.export_path, 'w', newline= '') as f:
            writer = csv.writer(f)
            writer.writerows(result)


if __name__ == '__main__':
    calculator = IncomeTaxCaluculator(UserData())






