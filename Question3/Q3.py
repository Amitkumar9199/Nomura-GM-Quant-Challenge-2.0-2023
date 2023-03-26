month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
         "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

def countLeapYears(d):
    years = d.year
    if(d.month <= 2):
        years -= 1
    return years//4 - years//100 + years//400

def get_diff(dt1, dt2):
    n1 = dt1.year * 365 + dt1.day
    for i in range(dt1.month - 1):
        n1 += month_days[i]
    n1 += countLeapYears(dt1)

    n2 = dt2.year * 365 + dt2.day
    for i in range(dt2.month - 1):
        n2 += month_days[i]
    n2 += countLeapYears(dt2)

    return n2 - n1

def find_diff(t_d, t_e):
    d1 = int(t_d[:2])
    d2 = int(t_e[:2])
    y1 = int(t_d[5:])
    y2 = int(t_e[5:])
    m1 = month[t_d[2:5]]
    m2 = month[t_e[2:5]]
    dt1 = Date(d1, m1, y1)
    dt2 = Date(d2, m2, y2)

    return get_diff(dt1, dt2)

def newdate(prev_date,freq):
    d1 = int(prev_date[:2])
    m1 = month[prev_date[2:5]]
    y1 = int(prev_date[5:])
    m2= int(freq[:-1])
    if m1+m2>12:
        y1+=1
        m1=m1+m2-12
    else:
        m1+=m2
    m1=list(month.keys())[m1-1]
    if d1<10:
        d1='0'+str(d1)
    else:
        d1=str(d1)
    return d1+m1+str(y1)

# Write a class C_ABC which can be constructed using the details of the financial product ABC.
class C_ABC:
    def __init__(self, t_start,t_final,freq,prd,F,C):
        self.t_start = t_start 
        self.t_final = t_final 
        self.freq = freq 
        self.prd = prd 
        self.F = F 
        self.C = C 

    def tau(self,small,large):
        return find_diff(small,large)/365
    
    def value_abc(self,tdeal,rdeal):

        mu=[]
        mu.append(0) # mu[0]=0
        cf=[]

        period_start_i = self.t_start
        for i in range(0, int(float(self.tau(self.t_start,self.t_final)) * 12 / int(self.freq[:-1]) + 5 )):
            period_end_i = newdate(period_start_i,self.freq) # period_end_i = period_start_i + freq
            if self.tau(period_end_i,self.t_final)<=0: # if period_end_i > t_final
                period_end_i = self.t_final
                cf.append(self.C*self.tau(period_start_i,period_end_i)*self.F*0.01)
                break
            else: # if period_end_i < t_final
                cf.append(self.C*self.tau(period_start_i,period_end_i)*self.F*0.01)
                period_start_i = period_end_i
        

        period_start_i = tdeal # period_start_i = tdeal
        
        for i in range(0,len(cf)): 
            period_end_i = newdate(period_start_i,self.freq) # period_end_i = period_start_i + freq
            if self.tau(period_end_i,self.t_final)<0: # if period_end_i > t_final
                period_end_i = self.t_final
                mu.append((cf[i]+mu[i])*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
            else: # if period_end_i < t_final
                mu.append((cf[i]+mu[i])*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
                period_start_i = period_end_i
                if (int)(period_start_i[:2])<self.prd: # if period_start_i[date] < prd
                    period_start_i = str(self.prd)+period_start_i[2:]


        vdeal=(self.F+mu[-1])/(1+rdeal*self.tau(tdeal,self.t_final)*0.01)
        return vdeal


    def rateofreturn_abc(self,tdeal,vdeal):
        val=0.0
        ok=[]
        while val<=100:
            mu=[]
            mu.append(0) # mu[0]=0
            cf=[]
            temp=val
            period_start_i = self.t_start
            for i in range(0, int(float(self.tau(self.t_start,self.t_final)) * 12 / int(self.freq[:-1]) + 5 )):
                period_end_i = newdate(period_start_i,self.freq) # period_end_i = period_start_i + freq
                if self.tau(period_end_i,self.t_final)<=0: # if period_end_i > t_final
                    period_end_i = self.t_final
                    cf.append(self.C*self.tau(period_start_i,period_end_i)*self.F*0.01)
                    break
                else: # if period_end_i < t_final
                    cf.append(self.C*self.tau(period_start_i,period_end_i)*self.F*0.01)
                    period_start_i = period_end_i
            

            period_start_i = tdeal # period_start_i = tdeal
            
            for i in range(0,len(cf)): 
                period_end_i = newdate(period_start_i,self.freq) # period_end_i = period_start_i + freq
                if self.tau(period_end_i,self.t_final)<0: # if period_end_i > t_final
                    period_end_i = self.t_final
                    mu.append((cf[i]+mu[i])*(1+temp*self.tau(period_start_i,period_end_i)*0.01))
                else: # if period_end_i < t_final
                    mu.append((cf[i]+mu[i])*(1+temp*self.tau(period_start_i,period_end_i)*0.01))
                    period_start_i = period_end_i
                    if (int)(period_start_i[:2])<self.prd: # if period_start_i[date] < prd
                        period_start_i = str(self.prd)+period_start_i[2:]


            tmp=(self.F+mu[-1])/(1+temp*self.tau(tdeal,self.t_final)*0.01)
            

            ok.append([abs(tmp-vdeal),val])
            val+=0.01
        ok.sort()
        mp={}
        for i in range(0,len(ok)):
            mp[ok[i][0]//1]=ok[i][1]
        ok=[]
        for i in mp:
            ok.append([i,mp[i]])
        ok.sort()
        return ok[0][1]

    def dvalue_drateofreturn_abc(self,tdeal,rdeal):
        
        mu=[]
        mu.append(0) # mu[0]=0
        cf=[]
        dmu_dr=[]
        dmu_dr.append(0) # dmu_dr[0]=0

        period_start_i = self.t_start # period_start_i = t_start
        for i in range(0, int(float(self.tau(self.t_start,self.t_final)) * 12 / int(self.freq[:-1]) + 5 )):
            period_end_i = newdate(period_start_i,self.freq) # period_end_i = period_start_i + freq
            if self.tau(period_end_i,self.t_final)<=0: # if period_end_i > t_final
                period_end_i = self.t_final
                cf.append(self.C*self.tau(period_start_i,period_end_i)*self.F*0.01)
                break
            else: # if period_end_i < t_final
                cf.append(self.C*self.tau(period_start_i,period_end_i)*self.F*0.01)
                period_start_i = period_end_i
        

        period_start_i = tdeal # period_start_i = tdeal
        for i in range(0,len(cf)): 
            period_end_i = newdate(period_start_i,self.freq) # period_end_i = period_start_i + freq
            if self.tau(period_end_i,self.t_final)<0: # if period_end_i > t_final
                period_end_i = self.t_final
                mu.append((cf[i]+mu[i])*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
                dmu_dr.append((cf[i]+mu[i])*(self.tau(period_start_i,period_end_i)*0.01) + dmu_dr[i]*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
            else: # if period_end_i < t_final
                mu.append((cf[i]+mu[i])*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
                dmu_dr.append((cf[i]+mu[i])*(self.tau(period_start_i,period_end_i)*0.01) + dmu_dr[i]*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
                period_start_i = period_end_i
                if (int)(period_start_i[:2])<self.prd: # if period_start_i[date] < prd
                    period_start_i = str(self.prd)+period_start_i[2:]


        dv_dr = 0
        dv_dr = dv_dr + ((self.F+mu[-1]) / ( (1+rdeal*self.tau(tdeal,self.t_final)*0.01)**2 ))* (-1) * self.tau(tdeal,self.t_final)*0.01
        

        dv_dr = dv_dr + (1/(1+rdeal*self.tau(tdeal,self.t_final)*0.01))*dmu_dr[-1]
        return dv_dr

    def d2value_drateofreturn2_abc(self,tdeal,rdeal):
        
        mu=[]
        mu.append(0) # mu[0]=0
        cf=[]
        dmu_dr=[]
        d2mu_dr2=[]
        dmu_dr.append(0) # dmu_dr[0]=0
        d2mu_dr2.append(0) # d2mu_dr2[0]=0
        
        period_start_i = self.t_start
        for i in range(0, int(float(self.tau(self.t_start,self.t_final)) * 12 / int(self.freq[:-1]) + 5 )):
            period_end_i = newdate(period_start_i,self.freq) # period_end_i = period_start_i + freq
            if self.tau(period_end_i,self.t_final)<=0: # if period_end_i > t_final
                period_end_i = self.t_final
                cf.append(self.C*self.tau(period_start_i,period_end_i)*self.F*0.01)
                break
            else: # if period_end_i < t_final
                cf.append(self.C*self.tau(period_start_i,period_end_i)*self.F*0.01)
                period_start_i = period_end_i
        

        period_start_i = tdeal # period_start_i = tdeal
        for i in range(0,len(cf)): 
            period_end_i = newdate(period_start_i,self.freq) # period_end_i = period_start_i + freq
            if self.tau(period_end_i,self.t_final)<0: # if period_end_i > t_final
                period_end_i = self.t_final
                mu.append((cf[i]+mu[i])*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
                dmu_dr.append((cf[i]+mu[i])*(self.tau(period_start_i,period_end_i)*0.01) + dmu_dr[i]*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
                d2mu_dr2.append(self.tau(period_start_i,period_end_i)*0.01*dmu_dr[i]*2 + d2mu_dr2[i]*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
            else: # if period_end_i < t_final
                mu.append((cf[i]+mu[i])*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
                dmu_dr.append((cf[i]+mu[i])*(self.tau(period_start_i,period_end_i)*0.01) + dmu_dr[i]*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
                d2mu_dr2.append(self.tau(period_start_i,period_end_i)*0.01*dmu_dr[i]*2 + d2mu_dr2[i]*(1+rdeal*self.tau(period_start_i,period_end_i)*0.01))
                period_start_i = period_end_i
                if (int)(period_start_i[:2])<self.prd: # if period_start_i[date] < prd
                    period_start_i = str(self.prd)+period_start_i[2:]


        dv_dr = 0
        dv_dr = dv_dr + ((self.F+mu[-1]) / ( (1+rdeal*self.tau(tdeal,self.t_final)*0.01)**2 ))* (-1) * self.tau(tdeal,self.t_final)*0.01
        dv_dr = dv_dr + (1/(1+rdeal*self.tau(tdeal,self.t_final)*0.01))*dmu_dr[-1]

        d2v_dr2 = 0
        d2v_dr2 = d2v_dr2 + ((self.F+mu[-1])* 2 * ((self.tau(tdeal,self.t_final)*0.01)**2))/((1+rdeal*self.tau(tdeal,self.t_final)*0.01)**3)
        d2v_dr2 = d2v_dr2 - (2 * (self.tau(tdeal,self.t_final)*0.01) * dmu_dr[-1]) / ((1+rdeal*self.tau(tdeal,self.t_final)*0.01)**2)
        d2v_dr2 = d2v_dr2 + (1/(1+rdeal*self.tau(tdeal,self.t_final)*0.01))*d2mu_dr2[-1]
        return d2v_dr2

# For the object o_abc = C_ABC(“03Feb2022”, “03Feb2024”, “3m”, 3, 100, 4)
# (1) Function = o_abc.value_abc, 𝑡𝑑𝑒𝑎𝑙 = “15Mar2023”, 𝑟𝑑𝑒𝑎𝑙 = 1.1
# (2) Function = o_abc.rateofreturn_abc, 𝑡𝑑𝑒𝑎𝑙 = “15Mar2023”, 𝑉𝑑𝑒𝑎𝑙 = 115.1
# (3) Function = o_abc.dvalue_drateofreturn_abc, 𝑡𝑑𝑒𝑎𝑙 = “27Apr2023”, 𝑟𝑑𝑒𝑎𝑙 = 2.37
# (4) Function = o_abc.d2value_ drateofreturn2_abc, 𝑡𝑑𝑒𝑎𝑙 = “07Jan2023”, 𝑟𝑑𝑒𝑎𝑙 = 5.3


o_abc = C_ABC("03Feb2022", "03Feb2024", "3m", 3, 100, 4)
print(o_abc.value_abc("15Mar2023", 1.1))
print(o_abc.rateofreturn_abc("15Mar2023", 115.1))
print(o_abc.dvalue_drateofreturn_abc("27Apr2023", 2.37))
print(o_abc.d2value_drateofreturn2_abc("07Jan2023", 5.3))

# 107.01366006546566
# 1.0000000000000007
# -0.7845049141872796
# 0.02056978870383186