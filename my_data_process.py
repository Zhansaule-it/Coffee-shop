class Solution:
    def my_data_process(self,param_1):
        output = {}
        #print(output)
        res = param_1[0].split(",")
        for i in res:
            if i != 'FirstName' and i != 'LastName' and i != 'UserName' and i != 'Coffee Quantity':
                output[i] = {}
        #print(output)
        file_input = [None]*7
        for i in range(len(param_1)):
            file_input[i] = param_1[i].split(",")
        m=0
        f=0
        for t in range(5):
            t+=1
            if file_input[t][0] == "Male":
                m+=1
            if file_input[t][0] == "Female":
                f+=1
        output['Gender'] = {'Male':m,'Female':f}
        y=0
        h=0
        for e in range(5):
            e+=1
            if file_input[e][4] == "yahoo.com":
                y+=1
            if file_input[e][4] == "hotmail.com":
                h+=1
        output['Email'] = {'yahoo.com':y,'hotmail.com':h}
        y=0
        h=0
        d=0
        for a in range(5):
            a+=1
            if file_input[a][5] == "21->40":
                y+=1
            if file_input[a][5] == "66->99":
                h+=1
            if file_input[a][5] == "41->65":
                d+=1
        output['Age'] = {'21->40':y,'66->99':h,'41->65':d}
        y=0
        h=0
        d=0
        c=0
        for ci in range(5):
            ci+=1
            if file_input[ci][6] == "Seattle":
                y+=1
            if file_input[ci][6] == "Detroit":
                h+=1
            if file_input[ci][6] == "Las Vegas":
                d+=1
            if file_input[ci][6] == "Chicago":
                c+=1
        output['City'] = {'Seattle':y,'Detroit':h,'Las Vegas':d,'Chicago':c}
        y=0
        h=0
        d=0
        c=0
        for di in range(5):
            di+=1
            if file_input[di][7] == "Safari iPhone":
                y+=1
            if file_input[di][7] == "Chrome Android":
                h+=1
            if file_input[di][7] == "Chrome":
                d+=1
        output['Device'] = {'Safari iPhone':y,'Chrome Android':h,'Chrome':d}
        y=0
        h=0
        d=0
        c=0
        for o in range(5):
            o+=1
            if file_input[o][9] == "afternoon":
                y+=1
            if file_input[o][9] == "morning":
                h+=1
        output['Order At'] = {'afternoon':y,'morning':h}
        #print(output)
        y = json.dumps(output)
        return y
#slo =["Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At", "Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon", "Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon", "Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon", "Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning", "Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]
#print(slo)
#print(my_data_process(slo))
