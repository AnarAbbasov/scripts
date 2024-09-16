select test_table.content from dbo.test_table
right JOIN dbo.test_fk_table
ON test_table.id=test_fk_table.PersonID

CREATE LOGIN anar   
    WITH PASSWORD = 'stroy@1234567';



select test_table.* from test_table WHERE
test_table.id in (select test_fk_table.PersonID from test_fk_table)



SELECT * from test_fk_table