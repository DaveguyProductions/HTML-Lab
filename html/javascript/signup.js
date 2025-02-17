function check_fields(email_s, name_s, password_s, date_s)
{
    let temp = document.getElementsByClassName("alert")
    if(temp.length > 0)
    {
        temp[0].parentNode.removeChild(temp[0])
    }

    let alrt = document.createElement("div")
    alrt.classList.add("alert")
    document.body.appendChild(alrt)

    current_time = Date.now()
    symbol_count = 0
    all_good = 0
    email_length = email_s.length


    if(email_s == "" || name_s == "" || password_s == "" || date_s == "")
    {
        alrt.appendChild( document.createTextNode("One or many fields are empty! "))
        all_good++
    }
    
    input_time = new Date(date_s)

    if(current_time - input_time < 410240376000)
    {
        alrt.appendChild( document.createTextNode("Ivalid age! "))
        all_good++
    }

    if(email_s[0] == '@')
    {
        alrt.appendChild( document.createTextNode("Email cannot start with an @ symbol! "))
        all_good++
    }

    if(email_s[email_length - 1] == '@')
    {
        alrt.appendChild( document.createTextNode("Email cannot end with an @ symbol! "))
        all_good++
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
        alrt.appendChild( document.createTextNode("Email address cannot have more than one @ symbol! "))
        all_good++
    }

    if(symbol_count < 1 && email_s != "")
    {
        alrt.appendChild( document.createTextNode("Email address must have @ symbol! "))
        all_good++
    }

    if(all_good == 0)
    {
        alrt.appendChild( document.createTextNode("Welcome!"))
    }
}
