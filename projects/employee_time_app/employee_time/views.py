from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from django.template import RequestContext

from datetime import date,datetime,time
from xlrd import open_workbook,xldate_as_tuple, XL_CELL_DATE
from calendar import monthrange

from holiday.models import Holiday, PersonalLeave, SpecialNotes

import os

def find_emp_row(uid, s, wb):
    count = 0
    rows = []
    for row in range(s.nrows):
        values = []
        if s.cell(row,0).value == uid:
            for col in range(s.ncols):
                if(s.cell(row,col).ctype==XL_CELL_DATE):
                    date_value = xldate_as_tuple(s.cell(row,col).value,wb.datemode)
                    values.append(date_value)
                else:
                    values.append(s.cell(row,col).value)
            rows.append(values)
            count = count + 1
    return rows

'''def opt_emp_row(rows):
    for i in range(len(rows)-1):
        if rows[i][2][2] == rows[i-1][2][2]:
            if rows[i][2][2] == rows[i+1][2][2]:
                del rows[i]
    return rows'''     

'''def opt_emp_row(rows):
    for i in range(len(rows)-1):
        if i != len(rows)-1:
            if rows[i][2][2] == rows[i-1][2][2]:
                if rows[i][2][2] == rows[i+1][2][2]:
                    del rows[i]
    return rows'''

def opt_emp_row(rows):
    for i in range(len(rows)):
        if (i != 0 and i != len(rows)-1):
            if rows[i][2][2] == rows[i-1][2][2]:
                if rows[i][2][2] == rows[i+1][2][2]:
                    rows[i].append('x')
    for row in rows:
        if len(row) == 4:
            rows.remove(row)
    return rows

def opt1_emp_row(rows):
    for row in rows:
        datelist = []; timelist = []
        datelist.append(row[2][0]); datelist.append(row[2][1]); datelist.append(row[2][2])
        timelist.append(row[2][3]); timelist.append(row[2][4]); timelist.append(row[2][5])
        row.append(datelist); row.append(timelist)
        del row[2]
    return rows

def opt2_emp_row(rows):
    for i in range(len(rows)):
        if i != len(rows)-1:
            if len(rows[i]) > 3:
                if rows[i][2][2] == rows[i+1][2][2]:
                    rows[i].append(rows[i+1][3])
                    del rows[i+1][3]
                else:
                    rows[i].append([])
        else:
            if len(rows[i]) > 3:
                rows[i].append([])

    for row in rows:
        if len(row) == 3:
            rows.remove(row)
    return rows

def opt3_emp_row(rows):
    for row in rows:
        if (row[3][0] == 10 and row[3][1] > 30):
            row.append('y')
        elif (row[3][0] > 10):
            row.append('y')
        else:
            row.append('n')
    return rows


def opt4_emp_row(rows):
    for row in rows:
        if len(row[4]) != 0:
            start_time = datetime(row[2][0], row[2][1], row[2][2], row[3][0], row[3][1])
            end_time = datetime(row[2][0], row[2][1], row[2][2], row[4][0], row[4][1])
            row.append(str(end_time - start_time))
        else:
            if row[3][0] >= 15:
                start_time = datetime(row[2][0], row[2][1], row[2][2], 15, 0)
                end_time = datetime(row[2][0], row[2][1], row[2][2], row[3][0], row[3][1])
                row.append(str(end_time - start_time))
            else:
                start_time = datetime(row[2][0], row[2][1], row[2][2], row[3][0], row[3][1])
                end_time = datetime(row[2][0], row[2][1], row[2][2], 15, 0)
                row.append(str(end_time - start_time))

def gen_full_month_record(rows):
    full_month = []
    emp_id = int(rows[0][0])
    emp_name = str(rows[0][1])
    no_of_days = monthrange(rows[0][2][0], rows[0][2][1])[1]
    for i in range(1, no_of_days + 1):
        daily_record = []
        record_date = [rows[0][2][0], rows[0][2][1], i]
        weekday = day_of_week(record_date)
        flag_day_matched = 0
        for row in rows:
            if cmp(record_date, row[2]) == 0:
                daily_record.append(emp_id); daily_record.append(emp_name); daily_record.append(record_date);daily_record.append(weekday)
                daily_record.append(row[3]); daily_record.append(row[4]); daily_record.append(row[5]); daily_record.append(row[6]);
                flag_day_matched = 1
                break
        if(flag_day_matched == 0):
            daily_record.append(emp_id); daily_record.append(emp_name); daily_record.append(record_date);daily_record.append(weekday)
            daily_record.append([]); daily_record.append([]); daily_record.append([]); daily_record.append([]);
        full_month.append(daily_record)

    return full_month

def gen_full_month_record_with_holiday(full_month):
    for row in full_month:
        record_date = str(row[2][0]) + '-' + str(row[2][1]) + '-' + str(row[2][2])
        try:
            h = Holiday.objects.get(holiday_date=record_date)
            row.append('holiday')
        except:
            row.append('on day')
    return full_month
    
def gen_full_month_record_with_personal_leave(full_month_with_holiday):
    for row in full_month_with_holiday:
        record_date = str(row[2][0]) + '-' + str(row[2][1]) + '-' + str(row[2][2])
        try:
            h = PersonalLeave.objects.get(leave_date=record_date, emp_id__emp_id = row[0])
            row.append(str(h.leave_name))
        except:
            row.append([])
    full_month_with_personal_leave = full_month_with_holiday
    return full_month_with_personal_leave

def gen_full_month_record_with_special_notes(full_month_with_personal_leave):
    for row in full_month_with_personal_leave:
        record_date = str(row[2][0]) + '-' + str(row[2][1]) + '-' + str(row[2][2])
        try:
            h = SpecialNotes.objects.get(note_date=record_date, emp_id__emp_id = row[0])
            row.append(str(h.note))
        except:
            row.append([])
    full_month_with_special_notes = full_month_with_personal_leave
    return full_month_with_special_notes

def day_of_week(record_date):
    no_of_day_in_week = datetime(record_date[0],record_date[1],record_date[2]).weekday()
    if(no_of_day_in_week == 0):
        return 'Monday'
    elif(no_of_day_in_week == 1):
        return 'Tuesday'
    elif(no_of_day_in_week == 2):
        return 'Wednesday'
    elif(no_of_day_in_week == 3):
        return 'Thursday'
    elif(no_of_day_in_week == 4):
        return 'Friday'
    elif(no_of_day_in_week == 5):
        return 'Saturday'
    else:
        return 'Sunday'

def print_rows(rows):
    for row in rows:
         print(row)


def home(request):
    context = RequestContext(request)
    return render(request, 'employee_time/base.html', {})
    #return HttpResponse('hello duniya')

def load_data(request):
    context = RequestContext(request)
    return render(request, 'employee_time/load.html', {})

def load_data_into_db(request):
    context = RequestContext(request)
    if request.method == 'POST':
        try:
            filename = request.POST['xlsfile']
            abs_path = 'D:/employee_time_app/xls_files/' + filename
            uid = float(request.POST['employee'])
            records = report(abs_path, uid)
            return render(request, 'employee_time/report.html', {'records': records[0], 'target_hour': records[1], 'achieved_hour': records[2], 'late_count': records[3]})
            #return HttpResponse('i need data grrrrrrrrrrrr')
        except:
            return HttpResponse('no such file')
    

def report_data(request):
    return HttpResponse('report data')


def get_holiday_count(full_month_with_holiday):
    count = 0
    for row in full_month_with_holiday:
        if row[8] == 'holiday':
            count += 1
    return count            

def get_late_entry_count(full_month_with_special_notes):
    count = 0
    for row in full_month_with_special_notes:
        if row[6] == 'y':
            count += 1
    return count

def get_month_total_hours_mins(full_month_with_holiday):
    total_hours  = 0
    total_mins = 0
    for row in full_month_with_holiday:    
        if len(row[7]) != 0:
            t = row[7].split(':')
            total_hours = total_hours + int(t[0])
            total_mins = total_mins + int(t[1])
    additional_hours = total_mins / 60
    remainder_mins = total_mins % 60
    total_hours += additional_hours
    total_hours_mins = [total_hours, remainder_mins]
    return total_hours_mins

def report(abs_path, uid):
    wb = open_workbook(abs_path)
    for s in wb.sheets():
         rows = find_emp_row(uid, s, wb)
         if len(rows) == 0:
             return HttpResponse('no records found for the given employee')
         else:
             opt_emp_row(rows)
             opt1_emp_row(rows)
             opt2_emp_row(rows)
             opt3_emp_row(rows)
             opt4_emp_row(rows)
             full_month = gen_full_month_record(rows)
             
             full_month_with_holiday = gen_full_month_record_with_holiday(full_month)
             no_of_holiday = get_holiday_count(full_month_with_holiday)
             no_of_working_day = len(full_month_with_holiday) - no_of_holiday
             target_working_hours = no_of_working_day * 9
             achieved_total_hours_mins = get_month_total_hours_mins(full_month_with_holiday)
             
             full_month_with_personal_leave = gen_full_month_record_with_personal_leave(full_month_with_holiday)
             full_month_with_special_notes = gen_full_month_record_with_special_notes(full_month_with_personal_leave)

             late_entry_count = get_late_entry_count(full_month_with_special_notes)

             for row in full_month_with_special_notes:
                 if len(row[2]) == 3: row[2] = str(row[2][0]) + '-' + str(row[2][1]) + '-' + str(row[2][2])
                 if len(row[4]) == 3: row[4] = str(row[4][0]) + ':' + str(row[4][1]) + ':' + str(row[4][2])
                 if len(row[5]) == 3: row[5] = str(row[5][0]) + ':' + str(row[5][1]) + ':' + str(row[5][2])

             for row in full_month_with_special_notes:
                 if row[4] == []: row[4] = 'N/A'
                 if row[5] == []: row[5] = 'N/A'
                 if row[6] == []: row[6] = 'N/A'
                 if row[7] == []: row[7] = 'N/A'
                 if row[9] == []: row[9] = 'N/A'
                 if row[10] == []: row[10] = 'N/A'

             return [full_month_with_special_notes, target_working_hours, achieved_total_hours_mins, late_entry_count]
