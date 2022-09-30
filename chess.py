#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Initialize TK"""

import time
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()


def func():
    print('button has been clicked')


for i in range(8):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)
root.rowconfigure(8, weight=1)
root.rowconfigure(9, weight=1)
root.rowconfigure(10, weight=1)
root.rowconfigure(11, weight=1)


def black_piece_check(row, column):
    for button_type in black_things_buttons:
        for button in button_type:
            info1 = button.grid_info()
            row1 = info1['row']
            column1 = info1['column']
            if row1 == row and column1 == column:
                return True
    return False


def white_piece_check(row, column):
    for button_type in white_things_buttons:
        for button in button_type:
            info1 = button.grid_info()
            row1 = info1['row']
            column1 = info1['column']
            if row1 == row and column1 == column:
                return True
    return False


turn_list = ['b']


def legal_moves(caller, row, column):

  # PAWNS

    L_of_legal_moves = []
    if caller['text'] == 'wp':
        check = white_piece_check(row - 1, column)
        if check == False:
            check = black_piece_check(row - 1, column)
            if check == False:
                L_of_legal_moves.append([row - 1, column])
        else:
            L_of_legal_moves = []
        if row == 8 and len(L_of_legal_moves) >= 1:
            check = white_piece_check(row - 2, column)
            if check == False:
                L_of_legal_moves.append([row - 2, column])
        if column != 0:
            check = white_piece_check(row - 1, column - 1)
            if check == False:
                check = black_piece_check(row - 1, column - 1)
                if check:
                    L_of_legal_moves.append([row - 1, column - 1])
        if column != 7:
            check = white_piece_check(row - 1, column + 1)
            if check == False:
                check = black_piece_check(row - 1, column + 1)
                if check:
                    L_of_legal_moves.append([row - 1, column + 1])
        return L_of_legal_moves
    if caller['text'] == 'bp':
        check = black_piece_check(row + 1, column)
        if check == False:
            check = white_piece_check(row + 1, column)
            if check == False:
                L_of_legal_moves.append([row + 1, column])
        else:
            L_of_legal_moves = []
        if row == 3 and len(L_of_legal_moves) >= 1:
            check = black_piece_check(row + 2, column)
            if check == False:
                L_of_legal_moves.append([row + 2, column])
        if column != 0:
            check = black_piece_check(row + 1, column - 1)
            if check == False:
                check = white_piece_check(row + 1, column - 1)
                if check:
                    L_of_legal_moves.append([row + 1, column - 1])
        if column != 7:
            check = black_piece_check(row + 1, column + 1)
            if check == False:
                check = white_piece_check(row + 1, column + 1)
                if check:
                    L_of_legal_moves.append([row + 1, column + 1])
        return L_of_legal_moves

    # KNIGHTS

    L_of_legal_moves = []
    if caller['text'] == 'wk':
        check = white_piece_check(row - 1, column - 2)
        if check == False:
            L_of_legal_moves.append([row - 1, column - 2])
        check = white_piece_check(row - 1, column + 2)
        if check == False:
            L_of_legal_moves.append([row - 1, column + 2])
        check = white_piece_check(row + 1, column - 2)
        if check == False:
            L_of_legal_moves.append([row + 1, column - 2])
        check = white_piece_check(row + 1, column + 2)
        if check == False:
            L_of_legal_moves.append([row + 1, column + 2])
        check = white_piece_check(row - 2, column - 1)
        if check == False:
            L_of_legal_moves.append([row - 2, column - 1])
        check = white_piece_check(row - 2, column + 1)
        if check == False:
            L_of_legal_moves.append([row - 2, column + 1])
        check = white_piece_check(row + 2, column - 1)
        if check == False:
            L_of_legal_moves.append([row + 2, column - 1])
        check = white_piece_check(row + 2, column + 1)
        if check == False:
            L_of_legal_moves.append([row + 2, column + 1])
        return L_of_legal_moves
    if caller['text'] == 'bk':
        check = black_piece_check(row - 1, column - 2)
        if check == False:
            L_of_legal_moves.append([row - 1, column - 2])
        check = black_piece_check(row - 1, column + 2)
        if check == False:
            L_of_legal_moves.append([row - 1, column + 2])
        check = black_piece_check(row + 1, column - 2)
        if check == False:
            L_of_legal_moves.append([row + 1, column - 2])
        check = black_piece_check(row + 1, column + 2)
        if check == False:
            L_of_legal_moves.append([row + 1, column + 2])
        check = black_piece_check(row - 2, column - 1)
        if check == False:
            L_of_legal_moves.append([row - 2, column - 1])
        check = black_piece_check(row - 2, column + 1)
        if check == False:
            L_of_legal_moves.append([row - 2, column + 1])
        check = black_piece_check(row + 2, column - 1)
        if check == False:
            L_of_legal_moves.append([row + 2, column - 1])
        check = black_piece_check(row + 2, column + 1)
        if check == False:
            L_of_legal_moves.append([row + 2, column + 1])
        return L_of_legal_moves

    # BISHOPS

    if caller['text'] == 'wb':
        for i in range(1, 7):
            check = white_piece_check(row - i, column - i)
            if check == True:
                break
            else:
                check = black_piece_check(row - i, column - i)
                L_of_legal_moves.append([row - i, column - i])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row - i, column + i)
            if check == True:
                break
            else:
                check = black_piece_check(row - i, column + i)
                L_of_legal_moves.append([row - i, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row + i, column + i)
            if check == True:
                break
            else:
                check = black_piece_check(row + i, column + i)
                L_of_legal_moves.append([row + i, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row + i, column - i)
            if check == True:
                break
            else:
                check = black_piece_check(row + i, column - i)
                L_of_legal_moves.append([row + i, column - i])
                if check == True:
                    break
        return L_of_legal_moves
    if caller['text'] == 'bb':
        for i in range(1, 7):
            check = black_piece_check(row - i, column - i)
            if check == True:
                break
            else:
                check = white_piece_check(row - i, column - i)
                L_of_legal_moves.append([row - i, column - i])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row - i, column + i)
            if check == True:
                break
            else:
                check = white_piece_check(row - i, column + i)
                L_of_legal_moves.append([row - i, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row + i, column + i)
            if check == True:
                break
            else:
                check = white_piece_check(row + i, column + i)
                L_of_legal_moves.append([row + i, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row + i, column - i)
            if check == True:
                break
            else:
                check = white_piece_check(row + i, column - i)
                L_of_legal_moves.append([row + i, column - i])
                if check == True:
                    break
        return L_of_legal_moves

    # ROOKS

    if caller['text'] == 'wr':
        for i in range(1, 7):
            check = white_piece_check(row - i, column)
            if check == True:
                break
            else:
                check = black_piece_check(row - i, column)
                L_of_legal_moves.append([row - i, column])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row, column + i)
            if check == True:
                break
            else:
                check = black_piece_check(row, column + i)
                L_of_legal_moves.append([row, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row + i, column)
            if check == True:
                break
            else:
                check = black_piece_check(row + i, column)
                L_of_legal_moves.append([row + i, column])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row, column - i)
            if check == True:
                break
            else:
                check = black_piece_check(row, column - i)
                L_of_legal_moves.append([row, column - i])
                if check == True:
                    break
        return L_of_legal_moves
    if caller['text'] == 'br':
        for i in range(1, 7):
            check = black_piece_check(row - i, column)
            if check == True:
                break
            else:
                check = white_piece_check(row - i, column)
                L_of_legal_moves.append([row - i, column])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row, column + i)
            if check == True:
                break
            else:
                check = white_piece_check(row, column + i)
                L_of_legal_moves.append([row, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row + i, column)
            if check == True:
                break
            else:
                check = white_piece_check(row + i, column)
                L_of_legal_moves.append([row + i, column])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row, column - i)
            if check == True:
                break
            else:
                check = white_piece_check(row, column - i)
                L_of_legal_moves.append([row, column - i])
                if check == True:
                    break
        return L_of_legal_moves
    if caller['text'] == 'wq':
        for i in range(1, 7):
            check = white_piece_check(row - i, column - i)
            if check == True:
                break
            else:
                check = black_piece_check(row - i, column - i)
                L_of_legal_moves.append([row - i, column - i])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row - i, column + i)
            if check == True:
                break
            else:
                check = black_piece_check(row - i, column + i)
                L_of_legal_moves.append([row - i, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row + i, column + i)
            if check == True:
                break
            else:
                check = black_piece_check(row + i, column + i)
                L_of_legal_moves.append([row + i, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row + i, column - i)
            if check == True:
                break
            else:
                check = black_piece_check(row + i, column - i)
                L_of_legal_moves.append([row + i, column - i])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row - i, column)
            if check == True:
                break
            else:
                check = black_piece_check(row - i, column)
                L_of_legal_moves.append([row - i, column])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row, column + i)
            if check == True:
                break
            else:
                check = black_piece_check(row, column + i)
                L_of_legal_moves.append([row, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row + i, column)
            if check == True:
                break
            else:
                check = black_piece_check(row + i, column)
                L_of_legal_moves.append([row + i, column])
                if check == True:
                    break
        for i in range(1, 7):
            check = white_piece_check(row, column - i)
            if check == True:
                break
            else:
                check = black_piece_check(row, column - i)
                L_of_legal_moves.append([row, column - i])
                if check == True:
                    break
        return L_of_legal_moves
    if caller['text'] == 'bq':
        for i in range(1, 7):
            check = black_piece_check(row - i, column - i)
            if check == True:
                break
            else:
                check = white_piece_check(row - i, column - i)
                L_of_legal_moves.append([row - i, column - i])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row - i, column + i)
            if check == True:
                break
            else:
                check = white_piece_check(row - i, column + i)
                L_of_legal_moves.append([row - i, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row + i, column + i)
            if check == True:
                break
            else:
                check = white_piece_check(row + i, column + i)
                L_of_legal_moves.append([row + i, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row + i, column - i)
            if check == True:
                break
            else:
                check = white_piece_check(row + i, column - i)
                L_of_legal_moves.append([row + i, column - i])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row - i, column)
            if check == True:
                break
            else:
                check = white_piece_check(row - i, column)
                L_of_legal_moves.append([row - i, column])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row, column + i)
            if check == True:
                break
            else:
                check = white_piece_check(row, column + i)
                L_of_legal_moves.append([row, column + i])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row + i, column)
            if check == True:
                break
            else:
                check = white_piece_check(row + i, column)
                L_of_legal_moves.append([row + i, column])
                if check == True:
                    break
        for i in range(1, 7):
            check = black_piece_check(row, column - i)
            if check == True:
                break
            else:
                check = white_piece_check(row, column - i)
                L_of_legal_moves.append([row, column - i])
                if check == True:
                    break
        return L_of_legal_moves
    if caller['text'] == 'wK':
        check = white_piece_check(row - 1, column)
        if check == False:
            L_of_legal_moves.append([row - 1, column])
        check = white_piece_check(row - 1, column - 1)
        if check == False:
            L_of_legal_moves.append([row - 1, column - 1])
        check = white_piece_check(row - 1, column + 1)
        if check == False:
            L_of_legal_moves.append([row - 1, column + 1])
        check = white_piece_check(row, column)
        if check == False:
            L_of_legal_moves.append([row, column])
        check = white_piece_check(row, column - 1)
        if check == False:
            L_of_legal_moves.append([row, column - 1])
        check = white_piece_check(row, column + 1)
        if check == False:
            L_of_legal_moves.append([row, column + 1])
        check = white_piece_check(row + 1, column)
        if check == False:
            L_of_legal_moves.append([row + 1, column])
            if column == 10:
                check = white_piece_check([row + 2, column])
                if check == False:
                    L_of_legal_moves.append([row + 2, column])
        check = white_piece_check(row + 1, column - 1)
        if check == False:
            L_of_legal_moves.append([row + 1, column - 1])
        check = white_piece_check(row + 1, column + 1)
        if check == False:
            L_of_legal_moves.append([row + 1, column + 1])
        return L_of_legal_moves
    if caller['text'] == 'bK':
        check = black_piece_check(row - 1, column)
        if check == False:
            L_of_legal_moves.append([row - 1, column])
        check = black_piece_check(row - 1, column - 1)
        if check == False:
            L_of_legal_moves.append([row - 1, column - 1])
        check = black_piece_check(row - 1, column + 1)
        if check == False:
            L_of_legal_moves.append([row - 1, column + 1])
        check = black_piece_check(row, column)
        if check == False:
            L_of_legal_moves.append([row, column])
        check = black_piece_check(row, column - 1)
        if check == False:
            L_of_legal_moves.append([row, column - 1])
        check = black_piece_check(row, column + 1)
        if check == False:
            L_of_legal_moves.append([row, column + 1])
        check = black_piece_check(row + 1, column)
        if check == False:
            L_of_legal_moves.append([row + 1, column])
        check = black_piece_check(row + 1, column - 1)
        if check == False:
            L_of_legal_moves.append([row + 1, column - 1])
        check = black_piece_check(row + 1, column + 1)
        if check == False:
            L_of_legal_moves.append([row + 1, column + 1])
        return L_of_legal_moves


def onClick(event):
    caller = event.widget
    if caller['text'][0] == turn_list[-1] and (caller['bg'] == 'grey'
            or caller['bg'] == 'grey'):
        print('the piece you used:')
        print(caller['text'][0])
        print('the last piece color:')
        print(turn_list[-1])
        print(' ')
        print('other player')
        print('turn list:')
        print(turn_list)
    else:
        info = caller.grid_info()
        row = info['row']
        column = info['column']
        if caller['text']:
            if caller['text'] != 'white' and caller['text'] != 'black':
                global highlight
                highlight = '#BBF6AD'
                moves = legal_moves(caller, row, column)
                for move in moves:
                    for button in elementlist:
                        infoofb = button.grid_info()
                        rowofb = infoofb['row']
                        columnofb = infoofb['column']
                        if move[0] == rowofb and move[1] == columnofb:
                            button['text'] = button['bg']
                            button['bg'] = highlight
                            button['fg'] = highlight
        print(caller['text'])
        saved(caller, row, column)


elementlist = []
for y in range(8):
    if y % 2:
        color = 'black'
        color2 = 'white'
    else:
        color = 'white'
        color2 = 'black'
    for i in range(8):
        if i % 2 == 0:
            x = color
        else:
            x = color2
        element = Button(root, bg=x, height=5, width=10, command=func)
        element.grid(row=i + 2, column=y)
        element.bind('<1>', onClick)
        elementlist.append(element)


def free_column(n):
    if n == 'b':
        Ldead = [-1]
        Ldead2 = [-1]
        for button_type in black_things_buttons:
            for button in button_type:
                infodead = button.grid_info()
                if infodead['row'] == 10:
                    Ldead.append(infodead['column'])
                if infodead['row'] == 11:
                    Ldead2.append(infodead['column'])
    if n == 'w':
        Ldead = [-1]
        Ldead2 = [-1]
        for button_type in white_things_buttons:
            for button in button_type:
                infodead = button.grid_info()
                if infodead['row'] == 0:
                    Ldead.append(infodead['column'])
                if infodead['row'] == 1:
                    Ldead2.append(infodead['column'])
    first_dead_row_max = max(Ldead)
    if first_dead_row_max == 7:
        second_dead_row_max = max(Ldead2)
        return second_dead_row_max + 1
    else:
        return first_dead_row_max + 1


def free_row(n):
    if n == 'b':
        w = False
        Ldead = [-1]
        Ldead2 = [-1]
        for button_type in black_things_buttons:
            for button in button_type:
                infodead = button.grid_info()
                if infodead['row'] == 10:
                    Ldead.append(infodead['column'])
                if infodead['row'] == 11:
                    Ldead2.append(infodead['column'])
    if n == 'w':
        w = True
        Ldead = [-1]
        Ldead2 = [-1]
        for button_type in white_things_buttons:
            for button in button_type:
                infodead = button.grid_info()
                if infodead['row'] == 0:
                    Ldead.append(infodead['column'])
                if infodead['row'] == 1:
                    Ldead2.append(infodead['column'])
    first_dead_row_max = max(Ldead)
    if w:
        if first_dead_row_max == 7:
            second_dead_row_max = max(Ldead2)
            return 1
        else:
            return 0
    else:
        if first_dead_row_max == 7:
            second_dead_row_max = max(Ldead2)
            return 11
        else:
            return 10


def over():
    root.destroy()


def saved(caller, row, column):
    try:
        global L
        L[1] = 'temp'
        if caller['bg'] == highlight:
            L[1] = [caller, row, column]
        else:
            L = []
            for element in elementlist:
                if element['text']:
                    element['bg'] = element['text']
                    element['text'] = ''
    except:
        if caller['text']:
            L = [[caller, row, column]]
            L.append('temp')
    if L[1] != 'temp':
        for element in elementlist:
            if element['text']:
                element['bg'] = element['text']
                element['text'] = ''
        for i in range(len(elementlist)):
            if elementlist[i]['bg'] == highlight:
                if elementlist[i].grid_info()['row'] == 8:
                    elementlist[i]['bg'] = elementlist[i + 3]['bg']
                else:
                    elementlist[i]['bg'] = elementlist[i + 2]['bg']

        # Flip position from destination to mover

        L[0][0].grid(row=L[1][1], column=L[1][2])
        info = L[0][0].grid_info()
        colour = L[0][0]['text'][0]
        if colour == 'b':
            for button_type in white_things_buttons:
                for button in button_type:
                    info1 = button.grid_info()
                    row1 = info1['row']
                    column1 = info1['column']
                    if row1 == L[1][1] and column1 == L[1][2]:
                        button.grid(row=free_row('w'),
                                    column=free_column('w'))
                        button['bg'] = 'red'
                        if button['text'] == 'wK':
                            ov = Button(root, bg='grey',
                                    text='Game Over\nBlack Wins',
                                    command=over,
                                    font=('Times New Roman', 20,
                                    'italic'))
                            ov.grid(row=5, column=3, columnspan=3,
                                    rowspan=3, sticky='nsew')
                        time.sleep(0.5)
        else:
            for button_type in black_things_buttons:
                for button in button_type:
                    info1 = button.grid_info()
                    row1 = info1['row']
                    column1 = info1['column']
                    if row1 == info['row'] and column1 == info['column'
                            ]:
                        button.grid(row=free_row('b'),
                                    column=free_column('b'))
                        button['bg'] = 'red'
                        if button['text'] == 'bK':
                            ov = Button(root, bg='grey',
                                    text='Game Over\nWhite Wins',
                                    command=over,
                                    font=('Times New Roman', 20,
                                    'italic'))
                            ov.grid(row=5, column=3, columnspan=3,
                                    rowspan=3, sticky='nsew')
                        time.sleep(0.5)
        turn_list.append(L[0][0]['text'][0])

#        #check if king moved for future castling ideas
#       #check if king moved for future castling ideas
#       """if L[0][0]['text'][1] == 'K':
#         if L[0][0]["text"] == 'wK':
#           if has_king_moved[0] == False and L[1][2] >= 4:
#             for liste in white_things_buttons:
#               for button in liste:
#                 print(button)
#                 if button['text'] == 'wr' and button.grid_info()['column'] == 7 and button.grid_info()['row'] == 9:
#                   if has_king_side_rook_moved[0] == False:
#                     button.grid(row=9, column=5)
#                     has_king_side_rook_moved[0] == True:
#
#           elif has_king_moved[0] == False and L[1][2] <= 3:
#             for liste in white_things_buttons:
#               for button in liste:
#                 print(button)
#                 if button['text'] == 'wr' and button.grid_info()['column'] == 0 and button.grid_info()['row'] == 9:
#                   if has_queen_side_rook_moved[0] == False:
#                     button.grid(row=9, column=3)
#                     has_queen_side_rook_moved[0] == True:
#           has_king_moved[0] == True
#
#
#           #check if king moved for future castling ideas
#         if L[0][0]["text"] == 'bK':
#           if has_king_moved[1] == False and L[1][2] >= 4:
#             for liste in white_things_buttons:
#               for button in liste:
#                 print(button)
#                 if button['text'] == 'br' and button.grid_info()['column'] == 7 and button.grid_info()['row'] == 2:
#                   if has_king_side_rook_moved[1] == False:
#                     button.grid(row=2, column=5)
#                     has_king_side_rook_moved[1] == True:
#
#           elif has_king_moved[1] == False and L[1][2] <= 3:
#             for liste in white_things_buttons:
#               for button in liste:
#                 print(button)
#                 if button['text'] == 'br' and button.grid_info()['column'] == 0 and button.grid_info()['row'] == 2:
#                   if has_queen_side_rook_moved[1] == False:
#                     button.grid(row=2, column=3)
#                     has_queen_side_rook_moved[1] == True:
#           has_king_moved[1] == True
#         print(turn_list)"""

        L = []


# Create a photoimage object of the image in the path

photo89 = PhotoImage(file='wp.png')

# Resize image to fit on button

photoimage89 = photo89.subsample(18, 18)

white_pawns_buttons = [Button(root, bg='grey', text='wp', command=func,
                       image=photoimage89) for i in range(8)]
i = 0
for element in white_pawns_buttons:
    element.grid(row=8, column=i)
    element.bind('<1>', onClick)
    i += 1

photo90 = PhotoImage(file='bp.png')

photoimage90 = photo90.subsample(18, 18)

black_pawns_buttons = [Button(root, bg='grey', text='bp', command=func,
                       image=photoimage90) for i in range(8)]
i = 0
for element in black_pawns_buttons:
    element.grid(row=3, column=i)
    element.bind('<1>', onClick)
    i += 1

photo91 = PhotoImage(file='wr.png')


photoimage91 = photo91.subsample(18, 18)

white_rooks_buttons = [Button(root, bg='grey', text='wr', command=func,
                       image=photoimage91) for i in range(2)]
i = 0
for element in white_rooks_buttons:
    element.grid(row=9, column=0 + 7 * i)
    element.bind('<1>', onClick)
    i += 1

photo92 = PhotoImage(file='br.png')


photoimage92 = photo92.subsample(18, 18)

black_rooks_buttons = [Button(root, bg='grey', text='br', command=func,
                       image=photoimage92) for i in range(2)]
i = 0
for element in black_rooks_buttons:
    element.grid(row=2, column=0 + 7 * i)
    element.bind('<1>', onClick)
    i += 1


photo93 = PhotoImage(file='wb.png')

photoimage93 = photo93.subsample(18, 18)

white_bishops_buttons = [Button(root, bg='grey', text='wb',
                         command=func, image=photoimage93) for i in
                         range(2)]
i = 0
for element in white_bishops_buttons:
    element.grid(row=9, column=2 + 3 * i)
    element.bind('<1>', onClick)
    i += 1

photo94 = PhotoImage(file='bb.png')

photoimage94 = photo94.subsample(18, 18)

black_bishops_buttons = [Button(root, bg='grey', text='bb',
                         command=func, image=photoimage94) for i in
                         range(2)]
i = 0
for element in black_bishops_buttons:
    element.grid(row=2, column=2 + 3 * i)
    element.bind('<1>', onClick)
    i += 1

photo95 = PhotoImage(file='wknight.png')

photoimage95 = photo95.subsample(18, 18)

white_knights_buttons = [Button(root, bg='grey', text='wk',
                         command=func, image=photoimage95) for i in
                         range(2)]
i = 0
for element in white_knights_buttons:
    element.grid(row=9, column=1 + 5 * i)
    element.bind('<1>', onClick)
    i += 1

photo96 = PhotoImage(file='bknight.png')

photoimage96 = photo96.subsample(18, 18)

black_knights_buttons = [Button(root, bg='grey', text='bk',
                         command=func, image=photoimage96) for i in
                         range(2)]
i = 0
for element in black_knights_buttons:
    element.grid(row=2, column=1 + 5 * i)
    element.bind('<1>', onClick)
    i += 1

photo97 = PhotoImage(file='bq.png')

photoimage97 = photo97.subsample(18, 18)

black_queen_button = [Button(root, bg='grey', text='bq', command=func,
                      image=photoimage97)]
for element in black_queen_button:
    element.grid(row=2, column=3)
    element.bind('<1>', onClick)

photo98 = PhotoImage(file='wq.png')


photoimage98 = photo98.subsample(18, 18)

white_queen_button = [Button(root, bg='grey', text='wq', command=func,
                      image=photoimage98)]
for element in white_queen_button:
    element.grid(row=9, column=3)
    element.bind('<1>', onClick)

photo99 = PhotoImage(file='bK.png')


photoimage99 = photo99.subsample(18, 18)

black_king_button = [Button(root, bg='grey', text='bK', command=func,
                     image=photoimage99)]
for element in black_king_button:
    element.grid(row=2, column=4)
    element.bind('<1>', onClick)


photo100 = PhotoImage(file='wK.png')


photoimage100 = photo100.subsample(18, 18)

white_king_button = [Button(root, bg='grey', text='wK', command=func,
                     image=photoimage100)]
for element in white_king_button:
    element.grid(row=9, column=4)
    element.bind('<1>', onClick)

white_things_buttons = []
white_things_buttons.append(white_bishops_buttons)
white_things_buttons.append(white_rooks_buttons)
white_things_buttons.append(white_knights_buttons)
white_things_buttons.append(white_pawns_buttons)
white_things_buttons.append(white_queen_button)
white_things_buttons.append(white_king_button)

black_things_buttons = []
black_things_buttons.append(black_bishops_buttons)
black_things_buttons.append(black_rooks_buttons)
black_things_buttons.append(black_knights_buttons)
black_things_buttons.append(black_pawns_buttons)
black_things_buttons.append(black_queen_button)
black_things_buttons.append(black_king_button)

root.mainloop()

