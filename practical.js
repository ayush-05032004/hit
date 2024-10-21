function isLeapYear(year){
    return(year % 4 === 0 && year % 100 !==0) || (year % 400 === 0);
}

function getDaysInMonth(month, year){
    switch(month){
        case 1: return 31;
        case 2: return isLeapYear(year) ? 29 : 28;
        case 3: return 31;
        case 4: return 30;
        case 5: return 31;
        case 6: return 30;
        case 7: return 31;
        case 8: return 31;
        case 9: return 30;
        case 10: return 31;
        case 11: return 30;
        case 12: return 31;
        default: return 0;
    }
}

function generateDatesForYear(year){
    let dates = [];
    for(let month = 1; month <= 12; month++){
        let daysInonth = getDaysInMonth(month, year);
        for(let day = 1; day <= daysInonth; day++){
            let dd = day.toString().padStart(2, '0');
            let mm = month.toString().padStart(2, '0');
            dates.push(`${dd}/${mm}/${year}`);
    }
    return dates;
}
}

let year = 2024;
console.log(generateDatesForYear(year));