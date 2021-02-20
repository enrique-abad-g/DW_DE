# DW_DE

# TO DO:

Pandas.to_sql erlaubt nur 'append' oder 'replace'. Es ist möglicherweise eine gute Idee, eine Funktion zu erstellen, die nur die relevanten Daten zu der Datenbank hochlädt (viele Daten sind schon da)

Ich sollte prüfen, ob 'Overperforming score' in einer anderen Tabelle enthalten sein könnte.

In der Produktion wird dieses Skript täglich ausgeführt. Es ist nötig:

1. nur die E-Mail vom Vortag herunterladen. Dies kann mit `report_messages = service.users().messages().list(userId='me',q='subject:"Your report is ready",after:{0}'.((date.today() - timedelta(days=1)).strftime('%Y/%m/%d'))).execute()` erfolgen.
2. Datenbanktabellen in einen Datenrahmen herunterladen (mit `pandas.from_sql`, da diese bereits Daten enthalten) und die Daten mit den aus der E-Mail zusammenführen.
