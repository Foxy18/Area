def area(x, y, R):
    #�������� �������������� (�, �) ����������� �������
    if (-R <= x <= 0 and 0 <= y <= R and (x + R)**2 + (y - R)**2 >= R**2) or \
    (-R < y < 0 and 0 < x < R and x**2 + y**2 <= R**2):
        return print('����� �������� � ����������� �������')
    return print('����� �� �������� � ����������� �������')
#���� ������
x, y, R = map(float, input('������� �������� �, �, R ����� ������: ').split())
#����� ������� ��� �������� �������������� (�, �) ����������� �������
area(x, y, R)

