function check_fields(email_s, name_s, password_s, date_s)
{
    current_time = Date.now()
    symbol_count = 0;
    email_length = email_s.length

    if(email_s == "" || name_s == "" || password_s == "" || date_s == "")
    {
        alert("One or many fields are empty!")
    }
    
    input_time = new Date(date_s)

    if(current_time - input_time < 410240376000)
    {
        alert("Ivalid age!")
    }

    if(email_s[0] == '@')
    {
        alert("Email cannot start with an @ symbol!")
    }

    if(email_s[email_length - 1] == '@')
    {
        alert("Email cannot end with an @ symbol!")
    }

    if(email_s != "")
    {
        for(i=0; i < email_length; i++)
        {
            if(email_s[i] == '@')
            {
                symbol_count++
            }
        }
    }

    if(symbol_count > 1)
    {
        alert("Email address cannot have more than one @ symbol!")
    }

    if(symbol_count < 1 && email_s != "")
    {
        alert("Email address must have @ symbol!")
    }
}

