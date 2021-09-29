
# create ticket class
class Ticket:
    def __init__(self, ticket_number, staff_id, creator_name, contact_email, description):
        self.ticket_number = ticket_number
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description

    def __str__(self):
        return f'{self.ticket_number} {self.staff_id} {self.creator_name} {self.contact_email} {self.description}'
    
    def __repr__(self):
        return f'{self.ticket_number} {self.staff_id} {self.creator_name} {self.contact_email} {self.description}'
        
# create ticketing system class
class TicketingSystem:
    def __init__(self):
        self.ticket_list = []
        # ticket counter is equiv to static field
        self.ticket_counter = 2000
    
    def create_ticket(self, staff_id, creator_name, contact_email, description):
        if creator_name == '':
            creator_name = 'Not specified'
        if contact_email == '':
            contact_email = 'Not specified'
        ticket_number = self.ticket_counter + 1
        self.ticket_counter += 1
        self.ticket_list.append(Ticket(ticket_number, staff_id, creator_name, contact_email, description))
        return ticket_number
    
    def get_ticket(self, ticket_number):
        for ticket in self.ticket_list:
            if ticket.ticket_number == ticket_number:
                return ticket
        return None
    
    def get_tickets_by_staff_id(self, staff_id):
        ticket_list = []
        for ticket in self.ticket_list:
            if ticket.staff_id == staff_id:
                ticket_list.append(ticket)
        return ticket_list
    
    def get_tickets_by_creator_name(self, creator_name):
        ticket_list = []
        for ticket in self.ticket_list:
            if ticket.creator_name == creator_name:
                ticket_list.append(ticket)
        return ticket_list
    
    def get_tickets_by_contact_email(self, contact_email):
        ticket_list = []
        for ticket in self.ticket_list:
            if ticket.contact_email == contact_email:
                ticket_list.append(ticket)
        return ticket_list
    
    def get_tickets_by_description(self, description):
        ticket_list = []
        for ticket in self.ticket_list:
            if ticket.description == description:
                ticket_list.append(ticket)
        return ticket_list
    
    def get_tickets_by_description_and_creator_name(self, description, creator_name):
        ticket_list = []
        for ticket in self.ticket_list:
            if ticket.description == description and ticket.creator_name == creator_name:
                ticket_list.append(ticket)
        return ticket_list
    
    def get_tickets_by_description_and_contact_email(self, description, contact_email):
        ticket_list = []
        for ticket in self.ticket_list:
            if ticket.description == description and ticket.contact_email == contact_email:
                ticket_list.append(ticket)
        return ticket_list
    
    def get_tickets_by_description_and_creator_name_and_contact_email(self, description, creator_name, contact_email):
        ticket_list = []
        for ticket in self.ticket_list:
            if ticket.description == description and ticket.creator_name == creator_name and ticket.contact_email == contact_email:
                ticket_list.append(ticket)
        return ticket_list
    
    def get_tickets_by_description_and_creator_name_and_contact_email_and_staff_id(self, description, creator_name, contact_email, staff_id):
        ticket_list = []
        for ticket in self.ticket_list:
            if ticket.description == description and ticket.creator_name == creator_name and ticket.contact_email == contact_email and ticket.staff_id == staff_id:
                ticket_list.append(ticket)
        return ticket_list
    
# test creating a ticket
ticketing_system = TicketingSystem()
ticket_1 = ticketing_system.create_ticket(
    'johns',
    'John Smith',
    'john.smith@gmail.com',
    'This is a test ticket'
)
ticket_2 = ticketing_system.create_ticket(
    'pinals',
    'Pinal Shah',
    'pinals@whitecliffe.ac.nz',
    'This is a test ticket'
)

ticket_1_expected = 2001
ticket_2_expected = 2002

print(ticket_1 == ticket_1_expected, ticket_2 == ticket_2_expected)
print(ticket_1, ticket_2)
print(ticket_1, ticket_2)

# test ticket list
list = ticketing_system.ticket_list

print(list)


