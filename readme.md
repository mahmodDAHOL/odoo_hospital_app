# Hospital Management System

This is a hospital management system developed using Odoo 17. The system includes module for managing patients, appointments, prescriptions, and pharmacy operations.

## Features

- **Hospital Module**: The system includes a hospital module with its icon for easy identification.
- **Patient Management**: The system allows for the management of patient records, including list and form views, search functionality, gender-specific submenus, and archived field with default filters.
- **Appointment Management**: Appointments can be scheduled and linked to patient records. The system includes status bars, activity components, doctor assignments, and control buttons for appointment state management.
- **Prescription and Pharmacy Operations**: The system allows for the creation of prescriptions with state and priority fields. It also includes pharmacy operations with currency and total price calculations.

## Additional Functionality

- **User Interface Enhancements**: Various UI enhancements have been implemented including image fields for patients, toggle widgets for patient tags, color widgets for patient tag data, and smart buttons to view patient appointments.
- **Data Management**: The system includes sequence generation with prefixes, default values using get_default, duplication behavior settings, SQL constraints, delete policies, and inverse compute functions.
- **Advanced Functionality**: Advanced features such as cancel appointment wizards with transient models, age calculation from birth date using API depends decorator, birthday alerts in patient forms, progress bars in appointment views, calendar views for appointments.

## Installation

To install the Hospital Management System on your Odoo 17 instance:

1. Clone the repository to your local machine.
2. Install the required dependencies as per the Odoo 17 documentation.
3. Load the module into your Odoo instance using the Odoo Apps interface or by placing it in the addons directory.

## Usage

Once installed in your Odoo instance:

1. Access the Hospital module from the main menu to manage hospital-related settings.
2. Use the Patient module to manage patient records including appointments and prescriptions.
3. Schedule appointments through the Appointment module and manage their status using control buttons.

## Contributing

If you would like to contribute to this project:

1. Fork this repository
2. Create a new branch (git checkout -b feature)
3. Make your changes
4. Commit your changes (git commit -am 'Add new feature')
5. Push to the branch (git push origin feature)
6. Create a new Pull Request

We welcome any contributions that enhance or add new features to this Hospital Management System.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need assistance with this Hospital Management System!
